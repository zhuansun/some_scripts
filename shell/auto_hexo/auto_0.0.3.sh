#!/bin/bash
# 自动发布博客文章


# 用户输入错误信息
function error(){
	cat <<- _EOF_
		命令不对, 输入 sh xxx.sh -a [note|geekbbang]
	_EOF_
}


# 连接本地docker，重置本地变更，拉取gitee最新的变更
function pull_gitee() {
	if [ "$1" = "geekbang" ] || [ "$1" = "note" ]; then
		echo "You chose to pull $1."
		docker exec -it hexo0.1 sh -c "cd /var/www/hexo/$1/source/_posts/$1 && git reset --hard && git pull"
		echo "$1 Already up to date."
	else
		echo 'only "geekbang" or "note."'
	fi
}

function deploy_hexo(){
	# 部署hexo
	docker exec -it hexo0.1 sh -c "cd /var/www/hexo/$1 && hexo clean && hexo g && hexo d"
}

function pulish_hexo(){
	# 发布hexo
	# 请注意：SSH 端口号和路径应根据需要进行更改
	ssh root@192.168.31.235 -p 2333 "cd /volume1/web/www/$1-page/ && git reset --hard && git pull"
}

# 程序运行期间，检查用户参数是否输入正确
if [[ ! $1 ]]; then
	error
	exit
fi

case $1 in
	-a )
		# 执行所有的步骤
		pull_gitee "$2"
		deploy_hexo "$2"
		pulish_hexo "$2"
		exit 0
		;;
	* )
		# 用户参数输入错误，不支持，展示错误信息，同时退出程序
		error
		exit -1
		;;
esac
