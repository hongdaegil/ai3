# #1.
# count=0
# for i in range(200,801,1):
#     if not i%5==0:
#         print("%d"%i,end=" ")
#         count=count+1
#         if count%10==0:
#             print()
            
# print("수:%d"%i)

# #2.
# print("-"*40)
# print("  cm   mm   m   inch")
# print("-"*40)
# for cm in range(1,101,1):
#     mm=cm*10.0
#     m=cm*0.01
#     inch=cm*0.3937
#     print("%d %d %d %d"%(cm, mm, m, inch))

#3.

# for i in range(1,11):
    #     print('*'*i)

#4.
# for i in range(10):
#     print('*'*(10-i))
# print()

# #5.
# number=input("숫자를 입력하세요:")
# total=0
# for a in range(1,11):
#     a=int(a)
# if a==1 or a==3 or a==5 or a==7 or a==9:
#     print("홀수입니다.%s"%a)

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
