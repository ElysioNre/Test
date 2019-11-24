
s = input('请输入一句话:')
for i in s:
    if i!=' ':
        print(chr(ord(i)-32),end='')
    else:
        print('',end=' ')
