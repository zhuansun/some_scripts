#!/bin/bash
# 在一个文件中，查找最长的一个字符串【使用参数展开】
for i; do
    if [[ -r $i ]]; then
        max_word=
        max_len=0
        for j in $(strings $i); do
            # 计算字符串的长度，在这里使用字符串展开
            #len=$(echo $j | wc -c)
            len=${#j}
            if (( len > max_len )); then
                max_len=$len
                max_word=$j
            fi
done
        echo "$i: '$max_word' ($max_len characters)"
    fi
done