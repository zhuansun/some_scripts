
用于同步本地和远程服务器 的文件

主要用于 远程# >本地

如果需要 本地# >远程，我不管

- 仅适用于 centos 7
- 确保本地可以免密登陆服务器的root用户，才可以使用
- 目前仅支持一种配置方式： 独立运行方式

主要采用的方式是守护进程的方法，emmm，，，著名的小红帽维护软件库，也是采用的这种方式

参考的大神博客： https://www.cnblogs.com/george-guo/p/7718515.html



-c :
  - 同样的，使用之前，你需要实现本地可以免密登陆服务器
  - 因为ssh命令不能直接输入密码进行登录

-s ：
	- 修改rsync.local中的path = /home/xlei/data/www  
	- 其他的不要改动

几个命令：
-c [ip] check  检查ip服务器上是否存在rsync服务，如果不存在会自动安装，如果已存在，会自动更新到最新版本
-d [ip] delete 删除ip服务上的rsync服务
-s [ip] start  在ip服务器上 启动rsync服务，并自动同步本地配置
-r [ip] [dir] rsync  开始同步服务器文件到本地[dir]目录中