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
    return m



n = int(input('请输入一个十进制数:'))
print(hex2(n))
