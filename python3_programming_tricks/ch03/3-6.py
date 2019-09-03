s = '    liushuo@qq.com   '
s.strip()
s.lstrip()
s.rstrip()
s = '====liushuo@qq.com===='
s.strip('=')
s = '=+-==liushuo@qq.com==--=+'
s.strip('=-+')
s2 = 'abc:1234'
s2[:3] + s2[4:]
s3 = '     abc    xyz   '
s3.replace(' ','')
s4 = '   \t   abc   \t    xyz   \n  '
import re
re.sub('[ \t\n]+', '', s4)
re.sub('\s+', '', s4)
s5 = 'abc1234xyz'
s5.translate({ord('a'): 'X', ord('b'): 'Y'})
s5.maketrans('abcxyz', 'XYZABC')
s5.translate(s5.maketrans('abcxyz', 'XYZABC'))
# 删除字符

s5.translate({ord('a'): None})
import unicodedata
unicodedata.combining(s5[1])

