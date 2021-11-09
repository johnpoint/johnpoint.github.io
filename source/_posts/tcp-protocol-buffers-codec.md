---
title: 用于 gnet 的 Protocol buffers 编解码器
date: 2021-09-17 18:30:00
tags:
  - gnet
  - tcp
  - Protocol buffers
  - codec
  - 笔记
toc: true
---

要写一个 TCP 服务端，实现处理在纯 TCP 流中传输的 Protocol buffers 数据。网络框架很早就选好了，用性能杰出的 [gnet](https://gnet.host/)，问题是 gnet 的示例库里面没有直接解析纯 Protocol buffers 的编解码器，于是乎只能自己动手了...

## 协议分析

从 TCP 流里面传过来的是经过简单处理的 Protocol buffers 数据，他在数据的头携带了这个数据包的长度信息，像是这样

```
[ 头 ][ 数据 ][ 头 ][ 数据 ][ 头 ][ 数据 ][ 头 ][ 数据 ][ 头 ][ 数据 ]
```

调用 golang 的 proto 官方库中的 `func DecodeVarint(b []byte) (uint64, int)` 方法可以从数据中拿到两个值，分别是 数据的完整长度、标明数据长度的头信息的长度。

由于没有特定的协议在包与包之间进行明显的划分，所以得用他的头数据来进行分包。

## 解码器

```go
// 储存连接内的相关信息
type DataStruct struct {
	fullLength   int
	lenNumLength int
	fullData     []byte
}

func (d *Codec) Decode(c gnet.Conn) ([]byte, error) {
	ctx, ok := c.Context().(context.Context)
	if !ok {
		err := c.Close()
		if err != nil {
			return nil, nil
		}
	}

    // 从上下文里面拿出这个连接的编解码器储存 struct
	r, ok := ctx.Value("codec").(DataStruct)
	if !ok {
		err := c.Close()
		if err != nil {
			return nil, nil
		}
	}

    // 读取缓冲区内的所有信息
	bytes := c.Read()

    // 判断是否已经开始读取包
	if len(r.fullData) == 0 {

        // 调用函数获取头中带的信息
		var fullLength uint64
		fullLength, r.lenNumLength = proto.DecodeVarint(bytes)
		r.fullLength = int(fullLength)
		fmt.Println(r.fullLength, r.lenNumLength)
		if r.fullLength == 0 {
			return nil, nil
		}
	}

    // 拿到当前时间已经被储存进 struct 的数据的长度
	fullDataLong := len(r.fullData)

    // 把读到的数据一把梭全部拼进 fullData
	r.fullData = append(r.fullData, bytes...)

    // 判断长度是否符合要求
	if len(r.fullData) >= r.fullLength+r.lenNumLength {
		c.ShiftN(r.fullLength + r.lenNumLength - fullDataLong)

        // 截取有效的数据
		res := r.fullData[r.lenNumLength : r.fullLength+r.lenNumLength]

        // 连接的缓存清空
		r.fullData = []byte{}
		ctx = context.WithValue(ctx, "codec", r)
		c.SetContext(ctx)
		return res, nil
	}

    // 移动读取指针
	c.ShiftN(len(bytes))
	ctx = context.WithValue(ctx, "codec", r)
	c.SetContext(ctx)
	return nil, nil
}
```

上面那种解码方式是目前看运行状况来说暂时没有出现问题的方法，下面那一种则比较节省内存，两种解码方式区别主要是在于调用的 Read 函数不同，前者是把 gnet 的 ring buffer 里面的内容全部读取出来，而后者是先把头读取出来，拿到了完整的数据长度信息之后调用 ReadN 函数直接准确的将包体取出。

```go
func (d *Codec) Decode(c gnet.Conn) ([]byte, error) {
	ctx, ok := c.Context().(context.Context)
	if !ok {
		err := c.Close()
		if err != nil {
			return nil, nil
		}
	}

    // 从上下文里面拿出这个连接的编解码器储存 struct
	r, ok := ctx.Value("codec").(DataStruct)
	if !ok {
		err := c.Close()
		if err != nil {
			return nil, nil
		}
	}
    
	if len(r.fullData) == 0 {
		_, bytes := c.ReadN(10)
		var fullLength uint64
		fullLength, r.lenNumLength = proto.DecodeVarint(bytes)
		r.fullLength = int(fullLength)
		fmt.Println(r.fullLength, r.lenNumLength)
		if r.fullLength == 0 {
			return nil, nil
		}
	}
    
	fullDataLong := len(r.fullData)
	n, bytes := c.ReadN(r.fullLength + r.lenNumLength - fullDataLong)
	r.fullData = append(r.fullData, bytes...)
	c.ShiftN(n)
	if len(r.fullData) >= r.fullLength+r.lenNumLength {
		res := r.fullData[r.lenNumLength :]
		r.fullData = []byte{}
		ctx = context.WithValue(ctx, "codec", r)
		c.SetContext(ctx)
		return res, nil
	}
	ctx = context.WithValue(ctx, "codec", r)
	c.SetContext(ctx)
	return nil, nil
}
```

在代码中也可以看见，头数据中的包体长度信息我是存在连接的上下文中的，所以在 gnet 触发连接打开的事件时需要将储存信息的 struct 塞进上下文中。

```go
func (es *EventServer) OnOpened(c gnet.Conn) (out []byte, action gnet.Action) {
	ctx := context.WithValue(context.Background(), "codec", DataStruct{})
	c.SetContext(ctx)
	return
}
```

## 编码器

编码器这个部分就非常简单了，直接调用 proto 库里面的 EncodeVarint 函数就可以生成这个包体的头，将头信息放在包体的前面就可以将这个数据发送到客户端了。

```go
func (d *Codec) Encode(c gnet.Conn, buf []byte) ([]byte, error) {
	buf = append(proto.EncodeVarint(uint64(len(buf))), buf...)
	return buf, nil
}
```


## 2021-11-09 更新

大意了，之前用上下文存储中间信息的方法有 **严重的性能问题**，在调用 golang 原生的 `context.WithValue` 方法时候，会在传入的上下文下面创建一个子上下文，这就导致了在一次又一次解码中，上下文树越来越庞大，而且每一层上下文内部都存储了本次解码的 `DataStruct`，造成内存泄漏的问题。

在苦苦查了好几天，并且修了几个有可能的内存泄漏隐患之后我才意识到这一点(秃头.jpg)

然后再看了下 `gnet.Conn` 的一个实现的 `Context()` 方法，发现他只是将我们传进去的东西存在了一个 map 里面，并不需要使用 `context` 相关的，所以简单的解决方法就是直接将 `DataStruct` 传进去，目前来看是解决了内存泄漏的问题，代码如下

```go
func (d *Codec) Decode(c gnet.Conn) ([]byte, error) {
	// 从上下文里面拿出这个连接的编解码器储存 struct
	r, ok := c.Context().(DataStruct)
	if !ok {
		err := c.Close()
		if err != nil {
			return nil, nil
		}
	}
    
	if len(r.fullData) == 0 {
		_, bytes := c.ReadN(10)
		var fullLength uint64
		fullLength, r.lenNumLength = proto.DecodeVarint(bytes)
		r.fullLength = int(fullLength)
		fmt.Println(r.fullLength, r.lenNumLength)
		if r.fullLength == 0 {
			return nil, nil
		}
	}
    
	fullDataLong := len(r.fullData)
	n, bytes := c.ReadN(r.fullLength + r.lenNumLength - fullDataLong)
	r.fullData = append(r.fullData, bytes...)
	c.ShiftN(n)
	if len(r.fullData) >= r.fullLength+r.lenNumLength {
		res := r.fullData[r.lenNumLength :]
		r.fullData = []byte{}
		c.SetContext(r)
		return res, nil
	}
	ctx = context.WithValue(ctx, "codec", r)
	c.SetContext(r)
	return nil, nil
}
```

```go
func (es *EventServer) OnOpened(c gnet.Conn) (out []byte, action gnet.Action) {
	var r = DataStruct{}
	c.SetContext(r)
	return
}
```

## 参考资料

- [Go 语言设计与实现 > 上下文 Context > 传值方法](https://draveness.me/golang/docs/part3-runtime/ch06-concurrency/golang-context/#614-%E4%BC%A0%E5%80%BC%E6%96%B9%E6%B3%95)