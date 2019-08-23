test-ice使用python+unittest+DDT框架封装，主体结构如下

/config   放置配置文件

/data    放置测试数据文件，.xslx文件，可以自动读取，利用DDT数据驱动

/log   日志生成存放目录

/model  ice文件放置目录，编译后文件、目录都生成在这里

/public    公共方法，读取文件、Unittest基类等

/testcase   用例写在这里，test开头，一般一个模块一个用例文件

/run  程序入口，一些初始化操作，用例执行方式