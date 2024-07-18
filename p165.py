#반복문 while
# sum=0
# i=1
# while i<=10:
#     sum=sum+1
#     print("i의값:%2d=>합계:%d"%(i,sum))
#     i=i+1
# print()

# i=1
# sum=0
# while i<=10:
#     sum=sum+1
#     i=i+1
# print("합계는%d"%sum)

# sum=0
# i=500
# while i<=600:
#     if i%5==0:
#         sum=sum+i
#     i=i+1
# print("5의배수합계:%d"%(sum))

# sum=0
# i=1
# while i<=1000:
#     if i%100!=0:
#         sum=sum+i
#     i=i+1
# print("100의배수합계:%d"%sum)

# s="Python is widely used by a number of big companies"
# i=0
# conut=0
# print("모음:",end=" ")
# while i <=len(s)-1:
#     if(s[i]=="a" or s[i]=="A" or s[i]=="e" or s[i]=="E" or s[i]=="i" or s[i]=="I" or  s[i]=="u" or s[i]=="U" or s[i]=="o" or s[i]=="O"):
#         conut=conut+1
#         print(s[i],end=" ")
#     i=i+1
# print()
# print("모음개수:%d"%conut)

# #자음
# s="Python is widely used by a number of big companies"
# i=0
# conut=0
# print("모음:",end=" ")
# while i <=len(s)-1:
#     if(s[i]!=" " and not(s[i]=="a" or s[i]=="A" or s[i]=="e" or s[i]=="E" or s[i]=="i" or s[i]=="I" or  s[i]=="u" or s[i]=="U" or s[i]=="o" or s[i]=="O")):
#         conut=conut+1
#         print(s[i],end=" ")
#     i=i+1
# print()
# print("자음개수:%d"%conut)

#숫자 2개를 입력 받아서 덧셈하기
# yN="y"
# while yN=="y":
#     a=int(input("첫번째 숫자를입력하세요:"))
#     b=int(input("두번째 숫자를입력하세요:"))
#     c=a+b
#     print("합계는%d"%c)
#     yN=input("계속 하시겠습니까?(y:계속, n:그만)")

# yN="y"
# while( yN=="y"):
#     w=input("문자1:")
#     s=input("문자2:")
#     ws=""
#     for i in range(len(w)+len(s)):
#         if i <= len(w)-1:
#             ws=ws+w[i]
#         if i <= len(s)-1:
#             ws=ws+s[i]

#     print(ws)
#     yN=input("계속할래요?(y/n)")

# yN="y"
# while True:
#     w=input("문자1:")
#     s=input("문자2:")
#     ws=""
#     for i in range(len(w)+len(s)):
#         if i <= len(w)-1:
#             ws=ws+w[i]
#         if i <= len(s)-1:
#             ws=ws+s[i]

#     print(ws)
#     yN=input("계속할래요?(y/n)")
#     if yN=='n':
#         break
