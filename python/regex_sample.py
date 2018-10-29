#-*- coding:utf-8 -*-

import re

pattern = r"ca"
text = "caabsacasca\\ . a "
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
print("\n")
# define the text
text = """
101   COM   Computers
205   MAT   Mathematics
189   ENG    English
""" 

# compile the regex and search the pattern
regex_num = re.compile('\d+')
s = regex_num.search(text)

print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(text[s.start():s.end()])
#print(regex_num.findall(text))
print("\n")

# number only
print(re.findall("[0-9]+",text) )
print(re.findall("\d+", text))

# 3 Upper string
print(re.findall("[A-Z]{3}", text) )

# 4以上
print(re.findall("[a-zA-Z]{4,}", text) )

# タプルで分ける
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
s = re.findall(course_pattern, text)
print( s )
print(type(s[0]) )