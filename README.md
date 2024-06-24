# sqlmapcheck_burp对burp suite的结果进行扫描
在后台的渗透测试中，不可能把每个接口都手动使用sqlmap跑一遍，尤其是较为庞大的系统，这个时候可以借助burpsuite，例如我的第一步就是进行xray被动扫描，那么肯定就需要把功能都点一遍，xray虽然也能跑注入，但是经大量的验证有些注入是不太准确的。
在target里会记录所有经过burp代理的站点和接口，这个时候我们把它保存成一个文件如：
![image](https://github.com/purple-WL/sqlmapcheck_burp/assets/63894044/ce3e369a-e51a-4581-86a9-aeced67d0965)
