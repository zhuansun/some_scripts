
# auto_hexo

自动部署hexo脚本版本说明

本脚本是个人编写，只适用我自己。说明一下情况：

- hexo所在服务器IP：52youyong.xyz
- hexo所属用户：blog
- hexo所在目录：~/app/zhuansun.github.io/

## 版本更新说明
我会不断的完善该功能，直到我可以简化我所有的操作。并且在完善的过程中，还可以不断学习shell的编程。


## 更新说明

### dev

#### 更新说明
dev 开发版本， 拥有最新的功能。但是都没有测试

- 新增：
	- 支持-c connect 一键连接到hexo所在的blog用户，避免输入ssh xxx...

- 更新：
	- 对于 -h 查看命令帮助的命令，新增了支持 --help 命令

#### 使用说明
- 支持 -u upload 上传本地多个md文件到hexo对应的source文件夹中
- 支持 -d delete 删除hexo中的source文件夹中的指定的多个md文件
- 支持 -g denerate 编译部署，等同于在hexo目录下执行 hexo clean && hexo g && hexo d
- 支持 -h help 查看本shell脚本的简单帮助及如何使用






### 0.0.2

#### 更新说明
没有功能性更新，只是shell脚本内部方法调用优化

#### 使用说明
- 支持 -u upload 上传本地多个md文件到hexo对应的source文件夹中
- 支持 -d delete 删除hexo中的source文件夹中的指定的多个md文件
- 支持 -g denerate 编译部署，等同于在hexo目录下执行 hexo clean && hexo g && hexo d
- 支持 -h help 查看本shell脚本的简单帮助及如何使用



### 0.0.1

#### 更新说明
最初版本，仅支持最简单的功能

#### 使用说明
- 支持 -u upload 上传本地多个md文件到hexo对应的source文件夹中
- 支持 -d delete 删除hexo中的source文件夹中的指定的多个md文件
- 支持 -g denerate 编译部署，等同于在hexo目录下执行 hexo clean && hexo g && hexo d
- 支持 -h help 查看本shell脚本的简单帮助及如何使用


