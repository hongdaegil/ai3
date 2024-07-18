# #1
# for i in range(1,201,1) :
#     if i==100 :
#         continue
#     print( i, end=" ")
# print()
# print("-" * 100)

#while
i=1
while i<=100:
    i=i+1#continue 무한반복이라 continue위로올리든지 break를 쓰자
    if i==100:
        continue
    print(i,end=" ")
print()