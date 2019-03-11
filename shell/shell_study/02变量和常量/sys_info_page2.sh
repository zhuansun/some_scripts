#!/bin/bash
# 系统报告查看，变量和常量 高级篇
TITLE="$HOSTNAME - 系统信息报告"
CURRENT_TIME="$(date "+%Y-%m-%d %H:%M:%S")"
TIME_STAMP="由用户：$USER 于 $CURRENT_TIME 生成"
echo "<HTML>
    <HEAD>
          <TITLE>$TITLE</TITLE>
    </HEAD>
    <BODY>
          <H1>$TITLE</H1>
          <P>$TIME_STAMP</P>
    </BODY>
</HTML>"
