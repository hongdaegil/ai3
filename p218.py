# qu=['s_hool','compu_er','deco_ation','wind_o','hi_tory']
# an=['c','t','r','w','s']
# for i in range(len(qu)):
#     q='%s:밑 줄에 들어갈 알파벳은?'%qu[i]
#     gu=input(q)
#     if gu==an[i]:
#         print("맞네요")77
#     else:
#         print("다시")

#2
# sc=[]
# while True:
#     x=int(input("성적을 입력하세요(종료시-1입력):"))
#     if x==-1:
#         break
#     else:
#         sc.append(x)
# sum=0
# for a in sc:
#     sum=sum+a
# avg=sum/len(sc)
# print('합계:%d,평균:%.2f'%(sum,avg))

# #3
# s=[64,89,100,85,77,58,79,67,96,87,87,36,82,98,84,76,63,69,53,22]
# soo=0
# woo=0
# mi=0
# yang=0
# ga=0

# i=0
# while i<len(s):
#     if  s[i]>=90 and s[i]<=100: 
#         soo=soo+1
#     if  s[i]<=89 and s[i]>=80: 
#         woo=woo+1
#     if  s[i]>=70 and s[i]<=79: 
#         mi=mi+1
#     if  s[i]<=69 and s[i]>=60: 
#         yang=yang+1
#     if  s[i]<=59 and s[i]>=50: 
#         ga=ga+1
#     i=i+1
# print('수:%d명'%soo)
# print('우:%d명'%woo)
# print('미:%d명'%mi)
# print('양:%d명'%yang)
# print('가:%d명'%ga)

#4
s=[[0,0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0,0],\
   [0,0,0,0,0,0,0,0,0,0],\
   [1,1,1,0,0,0,0,0,1,0],\
   [0,0,0,0,0,1,0,0,0,0],\
   [0,1,0,0,0,1,0,1,0,0],\
   [0,0,0,0,0,0,1,0,0,0],\
   [1,0,1,0,0,0,0,0,0,1]]
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j]==0:
            print('%3s'%'☆',end="")
        else:
             print('%3s'%'★',end="")
    print()
