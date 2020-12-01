# 开发者：Lingyu
# 开发时间：2020/12/1 21:25
print('-------------选择结构--------')
print('-------------单分支结构--------')  # 如果。。。就。。。
money = 1000
s = float(input('您要取出的金额为:'))
if money >= s:  # 比较运算符，：加回车
    print('交易成功')  # 以下均Tab，表示在if条件分支内
    money = money - s
    print('您的余额为:', money)
    print('交易结束')
