#!/bin/bash
#posit-param: script to view command line parameters
# 位置参数：查看命令行参数的脚本
cat <<- _EOF_
\$0 = $0
\$1 = $1
\$2 = $2
\$3 = $3
\$4 = $4
\$5 = $5
\$6 = $6
\$7 = $7
\$8 = $8
\$9 = $9
_EOF_
