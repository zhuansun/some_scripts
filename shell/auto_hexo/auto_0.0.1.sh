#!/bin/bash
# 自动发布博客文章

:<<BLOCK
-u 上传多个指定文件到hexo中
-d 删除hexo中指定的多个文件
-g 开始部署
-h 查看帮助
BLOCK

# 用户输入错误信息
function error(){
	cat <<- _EOF_
		命令不对,输入 -h 查看帮助
	_EOF_
}

# 帮助信息
function help(){
	cat <<- _EOF_
		-u 上传多个指定文件到hexo中 : auth.sh -u xxx xxx xxx
		-d 删除hexo中指定的多个文件 : auth.sh -d xxx xxx xxx
		-g 开始部署 : auth.sh -g
		-h 查看帮助 : auth.sh -h
	_EOF_
}

# 程序运行期间，检查用户参数是否输入正确
if [[ ! $1 ]]; then
	error
	exit
fi


case $1 in
	-h )
		# 输出帮助,程序结束
		help
		exit 0
		;;
	-u )
		# 开始上传本地文件到hexo中
		# $# 获取命令行参数个数
		# 参数检查上传文件，确保所有的文件，都真实存在
		for i; do
			# 跳过命名行的第一个参数 -u -p -h 等
			if [[ $i =~ "-" ]]; then
				continue
			fi
			# 使用 -f 判断文件是否存在
			if [[ ! -f $i ]]; then
				echo "【 $i 】文件不存在,请确认文件目录"
				exit -1
			fi
		done
		# 在来一次for循环，开始上传文件
		for i; do
			# 跳过命名行的第一个参数 -u -p -h 等
			if [[ $i =~ "-" ]]; then
				continue
			fi
			if [[ -f $i ]]; then
				scp -P 22 $i blog@52youyong.xyz:~/app/zhuansun.github.io/source/_posts
				echo " 文件 $i 上传完成！！！"
			fi
		done
		exit 0
		;;
	-d )
		# 删除服务器上的文件
		echo "删除服务器上的文件"
		# for循环，开始删除文件
		for i; do
			# 跳过命名行的第一个参数 -u -p -h 等
			if [[ $i =~ "-" ]]; then
				continue
			fi
			ssh blog@52youyong.xyz "cd ~/app/zhuansun.github.io/source/_posts && rm -rf $i"
			echo " 文件 $i 删除完成！！！"
		done
		exit 0
		;;	
	-g )
		# 部署hexo
		echo "部署hexo"
		ssh blog@52youyong.xyz "cd ~/app/zhuansun.github.io && hexo clean && hexo g && hexo d"
		exit 0
		;;
	* )
		# 用户参数输入错误，不支持，展示错误信息，同时退出程序
		error
		exit -1
		;;
esac
