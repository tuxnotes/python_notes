# 以/var/log/dpkg.log.1为例


f = open('/var/log/dpkg.log.1')
log = f.read() # 实际工程中以行读取

import re

# re.sub(p, r, s)替换函数，p- pattern, r-替换部分，s-字符串
re.sub(r'(?P<d>\d{4})-(?P<m>\d{2})-(?P<y>\d{2})', r'\2/\3/\1', log)
re.sub(r'(?P<d>\d{4})-(?P<m>\d{2})-(?P<y>\d{2})', r'\g<m>/\g<d>/\g<y>', log)

# '\2' , \ 是一个转义字符，真正的表达方式是'\\2'，简洁的办法是r'\2',通常正则都要使用
# r，避免转义字符干扰, ?P用于为正则表达式的组命名

