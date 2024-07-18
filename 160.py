'''
a=2
for b in range(1,10):
    print("%dx%d=%d"%(a,b,a*b))

print("-"*30)

for a in range(2,10):
    for b in range(1,10):
        print("%dx%d=%d"%(a,b,a*b))
print("-"*30)


for i in range(5):
    for j in range(10):
        print("*",end=" ")
    print()
    '''

for i in range(10):
    for j in range(0,i,1):
        print(i,end=" ")
    print()

# for i in range(9,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()