# !/bin/bash
#  自动同步


#  用户输入错误信息
function error(){
	cat <<- _EOF_
		命令不对,输入 -h 或者 # help 查看帮助
	_EOF_
}

function help(){
	cat <<- _EOF_
		-c [ip] check  检查ip服务器上是否存在rsync服务，如果不存在会自动安装，如果已存在，会自动更新到最新版本
		-d [ip] delete 删除ip服务上的rsync服务
		-s [ip] start  在ip服务器上 启动rsync服务，并自动同步本地配置
		-r [ip] [dir] rsync  开始同步服务器文件到本地[dir]目录中
	_EOF_
}


#  检测服务器上是否安装了rsync,如果没安装，就安装 install ，否则，更新成最新版update
function check_update(){
	creult=$(ssh root@$2 "rpm -q rsync")
	# creult="package httpd is not installed"
	echo $creult
	if [[ "$creult" =~ "not installed" || "$creult" =~ "未安装" ]]; then
		#  匹配中英文
		echo "还未安装rsync，开始安装"
		ssh root@$2 "yum install rsync"
	else
		echo "已安装rsync，开始更新"
		ssh root@$2 "yum update rsync"
		
	fi
}

#  删除rsync包
function delete_rsync(){
	ssh root@$2 "yum erase rsync"
}




#  配置rsync
function start_rsync(){

	# 将本地文件先上传到服务器，然后同步之后，再删掉它
	scp -P 22 ./rsync.local root@$2:/etc/
	scp -P 22 ./web.passwd root@$2:/etc/
	# 修改passwd的权限
	ssh root@$2 "chmod 600 /etc/web.passwd"
	# 同步配置
	ssh root@$2 "cat /etc/rsync.local > /etc/rsyncd.conf"
	# 删除配置文件
	ssh root@$2 "rm -rf /etc/rsync.local"
	# 重启服务
	ssh root@$2 "service xinetd restart"
	# 检查服务
	ssh root@$2 "netstat -ntpl | grep 873"

}


#  开始同步
function auto_sync(){
	echo "正在准备同步数据到-->，请输入数据同步密码,如果忘记可以查看web.passwd： " $3
	rsync -avzP web@$2::web1 $3

	# 同步完之后，需要修复文件权限
	echo "数据已经同步完毕，如果打不开，请自行修复文件所属用户和所属权限"
}

#  程序运行期间，检查用户参数是否输入正确
if [[ ! $1 ]]; then
	error
	exit
fi

case $1 in
	-h | --help )
		# 输出帮助,程序结束
		help
		exit 0
		;;
	-c )
		check_update $*
		exit 0
		;;
	-d )
		delete_rsync $*
		exit 0
		;;
	-s )
		start_rsync $*
		exit 0
		;;
	-r )
		auto_sync $*
		exit 0
		;;
esac








