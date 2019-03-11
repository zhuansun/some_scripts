#!/bin/bash
# 完善sys_info_page程序
# 对report_home_space函数添加for循环

# y运行该程序 sys_info_page -f -i

# basename表示取出路径名，只展示文件本身的名字。
PROGNAME=$(basename $0)
TITLE="$HOSTNAME - 系统信息报告"
CURRENT_TIME="$(date "+%Y-%m-%d %H:%M:%S")"
TIME_STAMP="由用户：$USER 于 $CURRENT_TIME 生成"

# 系统运行时间
function report_uptime () {
	cat <<- _EOF_
		<H2>系统运行时间<H2>
		<PRE>$(uptime)</PRE>
	_EOF_
	return
}

# 磁盘剩余空间量
function report_disk_space () {
	cat <<- _EOF_
		<H2>磁盘剩余空间量</H2>
		<PRE>$(df -h)</PRE>
	_EOF_
	return
}

# 用户目录使用量
function report_home_space () {
	# 声明两个局部变量
	local format="%8s%10s%10s\n"
	local i dir_list total_files total_dirs total_size user_name

	# 如果是root用户
	if [[ $(id -u) -eq 0 ]]; then

		dir_list=/home/*
		user_name="All Users"
		
	else
		# 普通用户
		dir_list=$HOME
		user_name=$USER

	fi

	echo "<H2>用户主目录 ($user_name)</H2>"

	#循环遍历dirlist
	for i in $dir_list; do
		total_files=$(find $i -type f | wc -l)
		total_dirs=$(find $i -type d | wc -l)
		total_size=$(du -su $i | cut -f 1)
		echo "<H3>$i</H3>"
		echo "<PRE>"
		printf "$format" "目录" "文件" "大小"
		printf "$format" "---" "---" "---"
		printf "$format" $total_dirs $total_files $ total_size
		echo "</PRE>"
	done


	return
}


# 程序帮助
function usage(){
	echo "$PROGNAME: usage: $PROGNAME [-f file | -i]"
	return
}

function write_html_file(){
	cat <<- _EOF_
		 <HTML>
		    <HEAD>
		          <TITLE>$TITLE</TITLE>
		    </HEAD>
		    <BODY>
		          <H1>$TITLE</H1>
		          <P>$TIME_STAMP</P>
		          $(report_uptime)
		          $(report_disk_space)
		          $(report_home_space)
		    </BODY>
		</HTML>
	_EOF_
	return
}

# 程序命令行选项
interactive=
filename=
# -n 表示不为空
while [[ -n $1 ]]; do
	case $1 in
		-f | --file )
			shift
			filename=$1
			;;
		-i | --interactive )
			interactive=1
			;;
		-h | --help )
			usage
			exit
			;;
		* )
			usage >$2
			exit 1
			;;
	esac
	shift
done

# 交互模式
if [[ -n $interactive ]]; then
	while [[ true ]]; do
		read -p "请输入输出文件名: " filename
		if [[ -e $filename ]]; then
			read -p "$filename 已经存在,是否覆盖？[y/n/q]" confirm
			case $confirm in
				y|Y )
					# 覆盖文件
					break
					;;
				q|Q )
					# 退出程序
					exit
					;;
				* )
					# 
					continue
					;;										
			esac
			# -z zero 字符串的长度为0
		elif [[ -z $filename ]]; then
			continue
		else
			break
		fi
	done
fi

# 创建输出文件
if [[ -n $filename ]]; then
	if touch $filename && [[ -f $filename ]]; then
		write_html_file > $filename
	else
		echo "$PROGNAME 无法写入 '$filename'" >&2
		exit 1
	fi
else
	write_html_file
fi


