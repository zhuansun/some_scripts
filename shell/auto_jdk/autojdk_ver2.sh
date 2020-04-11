#!/bin/bash


{

	#如果文件夹不存在，创建文件夹
	if [ ! -d "/opt/java" ]; then
	  mkdir /opt/java
	fi

	if [ ! -d "/opt/maven" ]; then
	  mkdir /opt/maven
	fi

	echo "==========================================="
	echo "==========================================="
	echo "============【准备下载jdk1.8】==============="
	echo "==========================================="
	echo "==========================================="


	wget -P /opt/java https://youdao-note-images.oss-cn-hangzhou.aliyuncs.com/jdk-8u141-linux-x64.tar.gz


	echo "==========================================="
	echo "==========================================="
	echo "============【准备下载maven3.6.3】==========="
	echo "==========================================="
	echo "==========================================="


	wget -P /opt/maven https://youdao-note-images.oss-cn-hangzhou.aliyuncs.com/apache-maven-3.6.3-bin.tar.gz


	echo "==========================================="
	echo "==========================================="
	echo "============【3s后开始安装配置jdk】==========="
	echo "==========================================="
	echo "==========================================="

	sleep 3

    # -f 参数判断 $file 是否存在

    file=~/.bash_profile

    if [ ! -f "$file" ]; then
      touch "$file"
    else
      echo '' > "$file"
    fi

	# 初始化.bash_profile
	cat << _EOF_ >>~/.bash_profile
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=\$PATH:\$HOME/bin

export PATH
_EOF_



	tar -zxvf /opt/java/jdk-8u141-linux-x64.tar.gz -C /opt/java
	cd /opt/java/jdk1.8.0_*
	java_home=`pwd`
	echo $java_home
	echo "export JAVA_HOME=${java_home}" >>~/.bash_profile 
	echo "export JRE_HOME=\$JAVA_HOME/jre" >> ~/.bash_profile
	echo "export CLASSPATH=.:\$JAVA_HOME/lib:\$JRE_HOME/lib" >> ~/.bash_profile

	echo "==========================================="
	echo "==========================================="
	echo "============【3s后开始安装配置maven】========="
	echo "==========================================="
	echo "==========================================="

	sleep 3

	tar -zxvf /opt/maven/apache-maven-3.6.3-bin.tar.gz -C /opt/maven
	cd /opt/maven/apache-maven-*
	maven_home=`pwd`
	echo $maven_home
	echo "export M2_HOME=${maven_home}" >> ~/.bash_profile 
	echo "export PATH=\$JAVA_HOME/bin:\$M2_HOME/bin:\$PATH" >> ~/.bash_profile 

	echo "==========================================="
	echo "==========================================="
	echo "============【正在生效..请稍等】=============="
	echo "==========================================="
	echo "==========================================="

	sleep 3

	source ~/.bash_profile

	echo "==========================================="
	echo "==========================================="
	echo "============【配置完成】====================="
	echo "==========================================="
	echo "==========================================="

	echo "maven 配置完成------>注意：如果不生效，请在手动执行一遍 ： source ~/.bash_profile"

	echo "git 可以使用  yum install git 快速安装。。。。"


}