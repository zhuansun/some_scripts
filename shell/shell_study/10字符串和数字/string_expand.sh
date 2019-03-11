#!/bin/bash
# 有大量的展开形式可用于操作字符串

# ${#param} 展开成由 param 所包含的字符串的长度
param="this is foo"
echo ${#param}

# ${param:offset} 从offset开始提取字符，直到末尾
parm="this is foo"
echo ${param:4}

# ${param:offset:length} 从offset开始提取字符，截取length个长度
param="this is foo"
echo ${param:4:2}

# ${param: offset:length} 从offset开始提取字符，截取length个长度 [如果offset是负数，则表示从后往前截取]
param="this is foo"
echo ${param: -5}
echo ${param: -5:3}

# ${param#pattern} 会从 param 删除 开头到第一个匹配 patten 的所有字符【在我电脑不好使啊】
param="i am a chinese, you are a dog."
echo ${param#a}
#输出结果应该是: m a chinese, you are a dog.


# ${param##pattern} 会从 param 删除 开头到最后一个匹配 patten 的所有字符【在我电脑不好使啊】
param="i am a chinese, you are a dog."
echo ${param##a}
#输出结果应该是:  dog.


# ${param%pattern} 同${param#pattern}，只不过这个从末尾开始清除

# ${param%%pattern} 同${param##pattern}，只不过这个从末尾开始清除

# ${param/pattern/string} 在 param 中查找第【一个】匹配 pattern 的字符串，用 string 替换它 ，/string不填，表示删除
param="i am a chinese, you are a dog."
echo ${param/a/fuck}

# ${param//pattern/string }在 param 中查找【所有】匹配 pattern 的字符串，用 string 替换它 ，/string不填，表示删除
param="i am a chinese, you are a dog."
echo ${param//a/fuck}

# ${param/#pattern/string} 在 param 中 【从头】查找匹配 pattern 的字符串，用 string 替换它 ，/string不填，表示删除

# ${param/%pattern/string} 在 param 中 【从尾】查找匹配 pattern 的字符串，用 string 替换它 ，/string不填，表示删除








