# 开发者：Lingyu
# 开发时间：2020/11/25 10:33
print('hello\nworld')  # \  +转义功能的首字母 n-->newline的首字母表示换行
print('hello\tworld')  # \  +t  t-->tab的首字母表示空出一个水平制表符的位置
print('hello\rworld')  # \  +r  r-->return的首字母表示回车
print('hello\bworld')  # \  +b  b-->backspace的首字母表示退回一格
print('hello\rme')
print('老师说:\'大家好\'')

# 原字符-->在字符串之前加上r或R，不希望字符串中的转义字符起作用
print(R'hello\bworld')
# 注意事项：最后一个字符不能是一个\，可以是\\
print(chr(0b100111001011000))  # 基于二进制返回字符
