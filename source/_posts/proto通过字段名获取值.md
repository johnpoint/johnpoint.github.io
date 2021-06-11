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
func FindByName(name string, msg protoreflect.Message) (has bool, value protoreflect.Value) {
	msgDesc := msg.Descriptor()
	for i := 0; i < msgDesc.Fields().Len(); i++ {
		if msgDesc.Fields().Get(i).Message() != nil {
			sonMsg := msgDesc.Fields().Get(i)
			has, value = FindByName(name, msg.Get(sonMsg).Message())
			if has {
				return
			}
		}
		if msgDesc.Fields().Get(i).Name() == protoreflect.Name(name) {
			return true, msg.Get(msgDesc.Fields().Get(i))
		}
	}
	return false, value
}
```

这个还考虑到了在 proto message 里面嵌套了 message 的一种写法，仅供参考