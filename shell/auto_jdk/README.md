

# auto_jdk


更新于2020年04月11日11:52:34，使用autojdk_ver.sh


一键配置jdk环境
- 使用环境：centos7
- root用户

使用脚本之前，需要先下载好，jdk和maven的压缩包，脚本里面有提供，在系统的任意一个目录执行下面两个命令：
- wget -P /opt/java https://youdao-note-images.oss-cn-hangzhou.aliyuncs.com/jdk-8u141-linux-x64.tar.gz
- wget -P /opt/maven http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/binaries/apache-maven-3.6.2-bin.tar.gz

执行完之后，使用本脚本；
- 脚本使用的时候，如果没有权限，需要先赋予权限：chmod -R 755 xxx
- 然后执行完之后，就可以了；
- 执行完之后，测试环境是否可以，如果不可以
- 需要手动 source ~/.bash_profile 是配置生效一下



如果遇到其他问题，自行解决！！

