#!/bin/bash


# wget -P /opt/java https://youdao-note-images.oss-cn-hangzhou.aliyuncs.com/jdk-8u141-linux-x64.tar.gz

tar -zxvf /opt/java/jdk-8u141-linux-x64.tar.gz -C /opt/java
cd /opt/java/jdk1.8.0_*
java_home=`pwd`
echo $java_home
echo "export JAVA_HOME=${java_home}" >>~/.bash_profile 
echo "export JRE_HOME=\$JAVA_HOME/jre" >> ~/.bash_profile
echo "export CLASSPATH=.:\$JAVA_HOME/lib:\$JRE_HOME/lib" >> ~/.bash_profile

# wget -P /opt/maven http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/binaries/apache-maven-3.6.2-bin.tar.gz
tar -zxvf /opt/maven/apache-maven-3.6.2-bin.tar.gz -C /opt/maven
cd /opt/maven/apache-maven-*
maven_home=`pwd`
echo $maven_home
echo "export M2_HOME=${maven_home}" >> ~/.bash_profile 
echo "export PATH=\$JAVA_HOME/bin:\$M2_HOME/bin:\$PATH" >> ~/.bash_profile 

echo "使配置生效"

source ~/.bash_profile

echo "配置完成"

mvn -v

echo "maven 配置完成------>注意：如果不生效，请在手动执行一遍 ： source ~/.bash_profile"

echo "git 可以使用  yum install git 快速安装。。。。"

