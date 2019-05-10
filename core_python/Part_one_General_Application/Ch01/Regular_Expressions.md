# Regular Expressions

## 1.1 Introduction/Motivation

**正则表达**：正则表达为文本的模式匹配，抽取，查找替换等高级功能提供了基础。简单来说，正则表达由一些字符和特殊符号组成的字符串，能够匹配多个字符串。

## 1.2 Special Symbols and Characters

### 1.2.1 Matching More Than One Regex Pattern with Alternation(|)

### 1.2.2 Matching Any Single Character(.)

(.)符号匹配除了换行符\n意外的任何字符(Python正则表达有一个选项，S，如果设置了，则能匹配换行符)。无论字母、数字、空格(不含"\n")、可打印字符、不可打印字符、还是一个符号，使用点号都能匹配。

### 1.2.3 从字符串起始或结尾或单词边界匹配

如果要匹配字符串的开始位置,就必须使用脱字符(^)或者特殊字符\A (反斜线和大写字母 A)。后者主要用于那些没有脱字符的键盘(例如,某些国际键盘)。同样,美元符号($)或者\Z将用于匹配字符串的末尾位置。

这些符号的模式与其他大多数模式是不同的，因为这些模式指定了位置或方位。

**匹配**：试图在字符串的开始位置进行匹配

**搜索**：试图从字符串的任何位置开始匹配

特殊字符\b和\B可以用来匹配字符边界

\b will match a pattern to a word boundary, meaning that a pattern must be at the beginning of a word, whether there are any characters in front of it (word in the middle of a string) or not (word at the beginning of a line).

\B will match a pattern only if it appears starting in the middle of a word (i.e., not at a word boundary)

| Regex Pattern | Strings Matched                                      |
| ------------- | ---------------------------------------------------- |
| the           | Any string containing the                            |
| \bthe         | Any word that starts with the                        |
| \bthe\b       | Matches only the word the                            |
| \Bthe         | Any string that contains but does not begin with the |

### 1.2.4 Creating Character Classes([])

点号用来匹配任意单个符号，当需要匹配特定字符的时候就需要([])

| Regex Pattern      | Strings Matched                                              |
| ------------------ | ------------------------------------------------------------ |
| b[aeiu]t           | bat, bet, bit, but                                           |
| [cr]\[23][dp]\[o2] | A string of four characters: first is "c" or "r", then "2" or "3", followed by "d" or "p", and finally, either "o" or "2". For example, c2do, r3p2, r2d2, c3po, etc. |

### 1.2.5 Denoting Ranges(-) and Negation(^)

| Regex Pattern      | Strings Matched                                              |
| ------------------ | ------------------------------------------------------------ |
| z.[0-9]            | "z" followed by any character then followed by a single digit |
| [r-u]\[env-y]\[us] | "r","s","t", or "u" followed by "e", "n", "v", "w", "x", or "y" followed by "u" or "s" |
| [^aeiou]           | A non-vowel character                                        |
| [^\t\n]            | Not a TAB or \n                                              |
| ["-a]              | In an ASCII system, all characters that fall between " and a, that is , between ordinals 34 and 97 |

### 1.2.6 Multiple Occurrence/Repetition Using Closure Operators (*,+,?,{})

the special symbols * , + , and ? , all of which can be used to match single, multiple,
or no occurrences of string patterns.

\*  0次或多次,任意次

\+ 1次或多次,至少1次

? 0次或1次，至多1次

| Regex Pattern                    | Strings Matched                                              |
| -------------------------------- | ------------------------------------------------------------ |
| [dn]ot?                          | "d" or "n" followed by an "o" and , at most, ont "t" after that; thus, do, no, dot, not |
| 0?[1-9]                          | Any numeric digit, possibly prepended with a "0". For example, the set of numeric representations of the months January to September, whether single or double-digits. |
| [0-9]{15,16}                     | Fifteen or sixteen digits(for example, credit card numbers)  |
| </?\[^>]+>                       | Stings that match all valid(and invalid) HTML tags           |
| [KQRBNP]\[a-h]\[1-8]-[a-h]\[1-8] | Legal chess move in "long algebraic" notation(move only, no capture, check,etc.); that is, strings that start with any of "K", "Q", "R", "B", "N", or "P" followed by a hyphenated-pair of chess   board grid location from "a1" to "h8" (and everything in between), with the first coordinate indicating the former position, and the second being the new position. |

\* , \+ , ? , {}称为close operators

?的意思是匹配0次或1次，但还有其他的意思：**如果?用在close operators后面，它会是正则表达引擎匹配尽量少的重复次数。

尽量少的重复次数的意思：当匹配模式中使用了grouping operators-- grouping operators即是分组操作符"()"--正则表达引擎会尽可能多的包含字符，这就是*贪婪模式*。但?会告诉正则表达引擎尽可能少的匹配字符，将剩下的字符留给接下来的匹配模式。

例如，现有如下字符串：

```bash
data = "Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8"
```

有如下匹配模式：

```python
patt1 = '.+(\d+-\d+-\d+)'
patt2 = '.+?(\d+-\d+-\d+)'
# 上面的两种匹配模式都用到了grouping operators,括号()
patt3 = '.+\d+-\d+-\d+'  # 此匹配模式没有用到grouping operators
```

如果用patt3，不带grouping operators的匹配模式进行匹配，将是如下结果：

```python
>>> re.match(patt3, data).group()  # entire match
'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
```

如果使用patt1，将是如下结果：

```python
>>> re.match(patt1, data).group(1)  # subgroup 1
'4-6-8'
```

上面这个模式使用了grouping operators, 但'.+'会从字符串开头一直到117159036，留给满足后面匹配模式最少的字符，后面的匹配模式即分组中的'\d+-\d+-\d+',此种模式即为贪婪模式。

如果使用patt2，将是如下结果：

```python
>>> re.match(patt2, data).group(1)  # subgroup 1
'1171590364-6-8'
```

此种模式为非贪婪模式，即将满足分组内的匹配模式的字符长度最大化。

关于贪婪模式和非贪婪模式请参考下面链接：

https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

**Greedy versus Non-Greedy**

When repeating a regular expression, as in `a*`, the resulting action is to consume as much of the pattern as possible. This fact often bites you when you’re trying to match a pair of balanced delimiters, such as the angle brackets surrounding an HTML tag. The naive pattern for matching a single HTML tag doesn’t work because of the greedy nature of `.*`.

\>>>

```
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print(re.match('<.*>', s).span())
(0, 32)
>>> print(re.match('<.*>', s).group())
<html><head><title>Title</title>
```

The RE matches the `'<'` in `'<html>'`, and the `.*` consumes the rest of the string. There’s still more left in the RE, though, and the `>` can’t match at the end of the string, so the regular expression engine has to backtrack character by character until it finds a match for the `>`. The final match extends from the `'<'` in `'<html>'` to the `'>'` in `'</title>'`, which isn’t what you want.

In this case, the solution is to use the non-greedy qualifiers `*?`, `+?`, `??`, or `{m,n}?`, which match as *little* text as possible. In the above example, the `'>'` is tried immediately after the first `'<'` matches, and when it fails, the engine advances a character at a time, retrying the `'>'` at every step. This produces just the right result:

\>>>

```
>>> print(re.match('<.*?>', s).group())
<html>
```

(Note that parsing HTML or XML with regular expressions is painful. Quick-and-dirty patterns will handle common cases, but HTML and XML have special cases that will break the obvious regular expression; by the time you’ve written a regular expression that handles all of the possible cases, the patterns will be *very*complicated. Use an HTML or XML parser module for such tasks.)

https://docs.python.org/3/library/re.html

The `'*'`, `'+'`, and `'?'` qualifiers are all *greedy*; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE `<.*>` is matched against `'<a> b <c>'`, it will match the entire string, and not just `'<a>'`. Adding `?` after the qualifier makes it perform the match in *non-greedy* or *minimal* fashion; as *few* characters as possible will be matched. Using the RE `<.*?>` will match only `'<a>'`.

### 1.2.7 Special Characters Representing Character Sets

use \d to indicate the match of any decimal digit

\D matches any non-decimal digit , same as \[^0-9]

\w used to denote the entire alphanumeric character class

\W

\s used for whitespace characters

\S

| Regex Pattern     | Strings Matched                                              |
| ----------------- | ------------------------------------------------------------ |
| \w+-\d+           | Alphanumeric string and number separated by a hyphen         |
| [A-Za-z]\w*       | Alphabetic first character; additional characters(if present) can be alphanumberic(almost equivalent to the set of valid Python identifiers) |
| \d{3}-\d{3}-\d{4} | American-format telephone numbers with an area code prefix, as in 800-555-1212 |
| \w+@\w+\\.com     | Simple e-mail address of the form XXX@YYY.com                |

### 1.2.8 Desinating Groups with Parenthese (())

限制已经实现匹配到字符串，去掉不匹配的字符串。但有事更关心匹配到的数据。我们不就需要知道整个字符串是否匹配我们的标准，还需要**提取**成功匹配的特定字符串或部分字符串。为了实现这个目的，需要使用括号()将正则表达式括起来。

A pair of parentheses(()) can accomplish either (or both) of the following when used with regular expressions:

 - Grouping regular expressions
 - Matching subgroups

One good example of why you would want to group regular expressions is when you have two different regexes with which you want to compare a sting. Another reason is to group a regex in order to use a repetition operator on the entire regex(as opposed to an individual character or character class).

One side effect of using parentheses is that the substring that matched the pattern is saved for future use. Theses subgroups can be recalled for the same match or search, or extracted for post-processing.

Why are matches of subgroups important?The main reason is that there are times when you want to extract the pattern \w+-\d+ but wanted save the alphabetic first part and the numeric second part individually? We might want to do thist because with any successful match, we might want to see just what those strings were that matched our regex patterns.

If we add parentheses to bot subpatterns such as (\w+\)-(\d+\) , then we can access each of the matched subgroups individually. Subgrouping is preferred because the alternative is to write code to determine we have a match, then execute another separate routine(which we also had to create) to parse the entire match just to extract both parts. Why not let Python do it; it's a supported feature of the *re* module, so why reinvent the wheel?

| Regex Pattern                     | Strings Matched                                              |
| :-------------------------------- | ------------------------------------------------------------ |
| \d+(\\.\d*)?                      | Strings representing simple floating point numbers; that is, any number of digits followed optionally by a single decimal point and zero or numeric digits, as in "0.004", "2", "75", etc. |
| (Mr?s?\\.)?[A-Z]\[a-z]*[A-Za-z-]+ | First name and last name, with a restricted first name(must start with uppercase; lowercase only for remainning letters, if any), the full name , prepended by an optional title of "Mr.", "Mrs.", "Ms.", or "M." , and a flexible last name allowing for multiple words, dashes, and uppercase letters |

### 1.2.9 Extension Notations

Extension notations begin with the question mark symbol (? . . .). They are generally used more to provide flags, perform look-ahead(or look-behind), or check conditionally before determining a match.

## 1.3 Regexes and Python

