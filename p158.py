#5.1
# number=input("숫자를 입력하세요:")
# total=0
# for a in range(1,11):
#     a=int(a)
# if a==1 or a==3 or a==5 or a==7 or a==9:
#     print("홀수입니다.%s"%a)
#5.2
# number=input("숫자를 입력하세요:")
# cnt=0
# for i in number:
#     nVal=int(i)
#     nVal%2==1
#     cnt+=1
# print("홀수의 갯수는 %d개입니다"%cnt)

#5.3
# for k in range(5):
#     for i in range(0,101,10):
#         print(i,end=" ")
#     print()

#5.4

for k in range(5):
    for i in range(1,k+6,1):
        print(i,end=" ")
    print(i-(k-1))   

4.
for i in range(5):
    print((5-i))
print()        

#6.
# kg=1
# print('-'*50)
# print('%7s %7s %7s'%("킬로그램","파운드","온스"))
# print("-"*50)
# for kg in range(100,201,2):
#     pound=kg*2.204623
#     ounce=kg*35.273962
#     print("%s%8.1f%8.1f"%(kg,pound,ounce))
# print("-"*50)