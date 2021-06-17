---
title: proto 通过字段名获取值
author: johnpoint
date: 2021-06-11 15:48:00
tags:
- proto
- golang
- 笔记
---

很久没有更新博客了，一方面是出去实习比在学校的时候忙，真的很多东西等着我去学，太可怕了，~~另一方面就是懒~~

protobuf 真是个好东西，就是在你不知道具体结构的时候想要拿到特定字段的值有点小麻烦，好不容易折腾出来了，写篇博客记录一下

```golang
func FindByName(name string, msg protoreflect.Message) (has bool, value protoreflect.Value, isList bool) {
	if name == "" {
		return false, *new(protoreflect.Value), false
	}
	msgDesc := msg.Descriptor()
	for i := 0; i < msgDesc.Fields().Len(); i++ {
		if msgDesc.Fields().Get(i).Kind() == protoreflect.MessageKind {
			sonMsg := msgDesc.Fields().Get(i)
			has, value, isList = FindByName(name, msg.Get(sonMsg).Message()) // type mismatch: cannot convert list to message
			if has {
				return has, value, isList
			}
		}
		if msgDesc.Fields().Get(i).Name() == protoreflect.Name(name) {
			return true, msg.Get(msgDesc.Fields().Get(i)), msgDesc.Fields().Get(i).IsList()
		}
	}
	return false, value, false
}
```

这个还考虑到了在 proto message 里面嵌套了 message 的一种写法，仅供参考

update: 

有点小坑，如果字段里面是个切片的话从源码那边看，使用 Interface() 函数获得的 interface 是这个切片的指针，通过反射拿到的类型是 Ptr，导致后续的处理变得有点麻烦，所以我直接在函数内部加了一手判断，直接判断是否为 List 类型，返回回来根据布尔值进行相应的处理。

```golang
func (v Value) Interface() interface{} {
	switch v.typ {
	case nilType:
		return nil
	case boolType:
		return v.Bool()
	case int32Type:
		return int32(v.Int())
	case int64Type:
		return int64(v.Int())
	case uint32Type:
		return uint32(v.Uint())
	case uint64Type:
		return uint64(v.Uint())
	case float32Type:
		return float32(v.Float())
	case float64Type:
		return float64(v.Float())
	case stringType:
		return v.String()
	case bytesType:
		return v.Bytes()
	case enumType:
		return v.Enum()
	default:
		return v.getIface()
	}
}

func (v Value) getIface() (x interface{}) {
	*(*ifaceHeader)(unsafe.Pointer(&x)) = ifaceHeader{Type: v.typ, Data: v.ptr}
	return x
}
```