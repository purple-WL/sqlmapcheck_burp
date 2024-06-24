# sqlmapcheck_burp对burp suite的结果进行扫描
在后台的渗透测试中，不可能把每个接口都手动使用sqlmap跑一遍，尤其是较为庞大的系统，这个时候可以借助burpsuite，例如我的第一步就是进行xray被动扫描，那么肯定就需要把功能都点一遍，xray虽然也能跑注入，但是经大量的验证有些注入是不太准确的。
在target里会记录所有经过burp代理的站点和接口，这个时候我们把它保存成一个文件如：
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/ce3e369a-e51a-4581-86a9-aeced67d0965)

保存的时候记得不要勾选base64加密，没有意义，无非就是多处理一步，保存下来其实是xml文件：
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/5196c54b-bef2-45b3-97ac-2e3f939a5fb2)
这个时候只要去解析这个xml文件的请求，并让sqlmap跑就行了，就是造轮子，只要把每一个请求使用-r参数跑就行，效果如下：
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/b1555eae-634f-4b4c-80c1-a9a646c18253)
结果会输出一个简易版的报告
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/c46cefb5-4089-402b-83aa-8b91f5373d20)
里面主要记录请求和payload
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/3164732b-84a7-43b4-a0fe-7b82f093d84e)



