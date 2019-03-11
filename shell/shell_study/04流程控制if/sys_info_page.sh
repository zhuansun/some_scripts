#!/bin/bash
# 继续我们之前得sys_info_page,系统信息报告，这次我们设置几个方法函数，进行调用
#!/bin/bash
# 系统报告查看，变量和常量 使用here document替代echo进行输出
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

	# 如果是root用户
	if [[ $(id -u) -eq 0 ]]; then
		cat <<- _EOF_
			<H2>用户目录使用量</H2>
			<PRE>$(du -sh /home/*)</PRE>
		_EOF_
	else
		# 普通用户
		cat <<- _EOF_
			<H2>用户目录使用量</H2>
			<PRE>$(du -sh $HOME)</PRE>
		_EOF_
	fi
	return
}


cat << _EOF_
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
