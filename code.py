def unicode(s):
    s = s.encode('utf-16be')
    print('UTF-16BE code',end=':')
    for x in s:
        print(hex(x),end=' ')
    print(' ')
    return 0

unicode('李白')
print('李白'.encode('gb2312'))
print('李白'.encode('gbk'))
print('李白'.encode('gb18030'))
print('李白'.encode('utf-8'))
print('李白'.encode('utf-16be'))
print('李白'.encode('utf-16le'))
