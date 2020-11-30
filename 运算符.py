# 开发者：Lingyu
# 开发时间：2020/11/30 20:50
print('----------算术运算符-------')
print(11 // 2)  # 整除运算符
print(11 % 2)  # 取余运算符
print(2 ** 3)  # 幂运算符
print(-11 // 2)  # 一正一负，向下取整=-5.5-->-6
print(-11 % 2)  # 余数=被除数-除数*商=-11-2*(-6)=1

print('----------赋值运算符-------')  # 从右向左赋值，详见笔记
a, b, c = 12, 13, 16
print(a, b, c)

# 交换赋值
a, b = 12, 18
print('交换赋值之前:', a, b)
b, a = a, b
print('交换赋值之后:', a, b)

print('----------比较运算符-------')  # 对变量及表达式的结果进行大小、真假等比较，输出结果为布尔类型
a, b = 10, 15
print(a > b)
print(a < b)
print(a <= b)  # 小于等于
print(a == b)  #
print(a != b)  # 不等于

a = 10
b = 10
print(a == b)  # 比较a和b的值是否相等
print(a is b)  # 比较a和b的标识(id)是否相等
print(id(a))
print(id(b))

lst1 = {11, 22, 33, 44}
lst2 = {11, 22, 33, 44}
print(lst1 == lst2)  # 比较lst1和lst2的值是否相等
print(lst1 is lst2)  # 比较lst1和lst2的标识(id)是否相等
print(id(lst1))
print(id(lst2))
