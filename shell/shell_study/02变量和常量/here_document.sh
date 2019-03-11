#!/bin/bash
# 介绍here document的简单实用： 以从ftp下载文件为例
# 在这个例子中，我们使用了 一个 here document 将一系列的命令传递到这个 ftp 程序中，为的是从一个远端 FTP 服务器 中得到README文件:
# << 和 <<- 的区别: 后者会忽略_EOF_中的tab缩进符
FTP_SERVER=ftp.nl.debian.org
FTP_PATH=/debian/dists/lenny/main/installer-i386/current/images/cdrom/debian
REMOTE_FILE=README
ftp -n <<- _EOF_
	open $FTP_SERVER
	user anonymous me@linuxbox
	cd $FTP_PATH
	hash
	get $REMOTE_FILE
	bye
_EOF_
ls -l $REMOTE_FILE