#!/bin/bash
# 算数展开


# number 十进制
# 0number 8进制
# 0xnumber 16进制
# base#number base进制

echo $((0xff))
echo $((17#23))


# 一元运算符 ： + - 表示正负
# 算数运算符 ： +  -  *  /  **  %   加 减  乘 除  乘方  取余
# 赋值运算符(参考下面例子) = 表示赋值，  ++  --  +=  -+ 等等运算符
foo=0
echo $foo
if [[ foo=5 ]]; then
	echo "it is true"
fi



# 位运算符 

# 逻辑运算符 <= >= <  >  ==  !=  && || 

# 三元表达式  expr1?expr2:expr3
