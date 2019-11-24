def hex2a(n):
    i = 1
    s = 0
    while n%1 != 0 :
        s = s + ((n*2)//1)/(10**i)
        n = (n*2)%1
        i = i+1
    return s

n = float(input('请输入十进制小数:'))
print(hex2a(n))
