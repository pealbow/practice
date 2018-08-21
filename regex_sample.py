#-*- coding:utf-8 -*-

import re

pattern = r"ca"
text = "caabsacasca"
repatter = re.compile(pattern)
matchOB = repatter.match(text)


if matchOB:
    print( matchOB )
    print( matchOB.group() )# マッチした文字列を返す # ca
    print( matchOB.start() )# マッチの開始位置を返す # 0
    print( matchOB.end() )# マッチの終了位置を返す # 2
    print( matchOB.span() ) # マッチの位置(start, end)を含むタプルを返す # (0, 2)

matchlist = re.findall(pattern, text)

print(matchlist)
