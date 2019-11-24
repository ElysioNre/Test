def hex2a(n):
    i = 1
    s = 0
    while n%1 != 0 :
        s = s + ((n*2)//1)/(10**i)
        n = (n*2)%1
        i = i+1
    return s

def hex2(n):
    s = ''
    a = []
    if n==1:
        a = ['1']
    while n>= 1:
        st = str(n%2)
        a.append(st)
        n = n//2
    a.reverse()
    m = s.join(a)
    m = int(m)
    return m

def hex2ab(n):
    print(int(hex2(int(n)))+hex2a(n%1))
    return 0

n = float(input('请输入十进制数字:'))
hex2ab(n)
