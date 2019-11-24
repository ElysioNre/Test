
n = float(input('请输入十进制整数:'))
k = int(input('请输入需转换进制:'))
i = 0
s = 0
n1 = int(n//1)

while  n1!=0:
    s = s+n1%k*(10**i)
    i = i+1
    n1 = n1//k

i = -1
s1 = 0
d = n%1

while d % 1!=0:
    s1 = s1+int(((d*k)))*(10**i)
    i = i-1
    d = (d*k)%1

print(s+s1)
