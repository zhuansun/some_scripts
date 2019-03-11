#!/bin/bash
# 自动发布博客文章


# 用户输入错误信息
function error(){
	cat <<- _EOF_
		命令不对,输入 -h 或者 --help 查看帮助
	_EOF_
}

# connect_hexo直接连接到hexo中，避免输入ssh了
function connect_hexo(){
	echo "#####################【正在打开连接】#####################"
	ssh blog@52youyong.xyz
}

# 帮助信息
function help(){
	cat <<- _EOF_
		-u upload 上传多个指定文件到hexo中
		-d delete 删除hexo中指定的多个文件
		-g denerate 开始部署
		-h help 查看帮助
		-c connect 连接到hexo
	_EOF_
}


# 上传文件
function upload_file(){
	# 上传文件前，检查文件
	echo "#####################【上传前文件检查】#####################"
	for i in $*; do
		# 跳过命名行的第一个参数 -u -p -h 等
		if [[ "$i" =~ "-" ]]; then
			continue
		fi
		# 使用 -f 判断文件是否存在
		if [[ ! -f "$i" ]]; then
			echo "【 $i 】文件不存在,请确认文件目录"
			exit -1
		fi
	done
	echo "#####################【上传前文件检查【完成】】#################"
	# 文件检查完毕后，开始上传
	echo "#####################【开始上传文件】#########################"
	for i in $*; do
		# 跳过命名行的第一个参数 -u -p -h 等
		if [[ $i =~ "-" ]]; then
			continue
		fi
		if [[ -f $i ]]; then
			scp -P 22 $i blog@52youyong.xyz:~/app/zhuansun.github.io/source/_posts
			echo " 文件 $i 上传完成！！！"
		fi
	done
	echo "#####################【所有文件上传【完成】】###################"
}


# 删除文件
function delete_file(){
	# 删除服务器上的文件
	echo "#####################【删除服务器上的文件】#####################"
	# for循环，开始删除文件
	for i in $*; do
		# 跳过命名行的第一个参数 -u -p -h 等
		if [[ "$i" =~ "-" ]]; then
			continue
		fi
		ssh blog@52youyong.xyz "cd ~/app/zhuansun.github.io/source/_posts && rm -rf $i"
		echo " 文件 $i 删除完成！！！"
	done
	echo "#####################【删除服务器上的文件【完成】】###############"
}

# 部署hexo
function deploy_hexo(){
	echo "#####################【开始部署hexo】#####################"
	ssh blog@52youyong.xyz "cd ~/app/zhuansun.github.io && hexo clean && hexo g && hexo d"
	echo "#####################【开始部署hexo【完成】】#####################"
}




# 程序运行期间，检查用户参数是否输入正确
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
	-u )
		# 上传本地文件到hexo中
		upload_file $*
		exit 0
		;;
	-d )
		# 删除
		delete_file $*
		exit 0
		;;	
	-g )
		# 部署
		deploy_hexo
		exit 0
		;;
	-c )
		# 部署
		connect_hexo
		exit 0
		;;	
	* )
		# 用户参数输入错误，不支持，展示错误信息，同时退出程序
		error
		exit -1
		;;
esac
