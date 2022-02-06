# tools
包含常用的工具，比如抓包、发包、脚本修改替换、mq收发消息、汇编、反汇编工具等。

### [rabbitmq发包工具](rabbitmq/rabbitmq_send_message.go)  

### [汇编代码函数表符号翻译]() 
把汇编代码中的符号表翻译成对应的函数名称
```
$ c++filt _ZNSt6vectorIiSaIiEEC2ESt16initializer_listIiERKS0_
std::vector<int, std::allocator<int> >::vector(std::initializer_list<int>, std::allocator<int> const&)
```
