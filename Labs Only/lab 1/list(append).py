L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L)

L1 = ['a', ['bb', 'cc'], 'd']
L1[1].append(0,'xx')
print(L1)

L2 = ['a', ['bb', 'cc'], 'd']
L2[1].extend([1, 2, 3])
print(L2)
