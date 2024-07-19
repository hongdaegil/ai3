# list1=[3,15,-12.5,'사과','딸기',True,False]
# list2=list(range(1,21,2))
# print(list1)
# print(list2)
# for i in range(7):
#     print( list1[6-i],end=" ")
# print('-'*50)    
# print(list2[::2])
# print(list2[-1::-2])

#응용문제
# list3=list(range(100,201,10))
# print(list3)
# cnt=0
# sum=0
# for i in list3:
#     cnt=cnt+1
#     sum=sum+i

# print("리스트의 갯수는 몇개%d입니다"%cnt)
# #합계구하기
# print("합계%d"%sum)
# #리스트의 갯수 구하기
# print(len(list))
# 

# colors=['빨간색','파란색','노란색','검정색','초록색']

# for color in colors:
#     print("나는 %s을 좋아해"%color)

# colors=['빨간색','노란색','파란색','검정색','초록색']
# n=len(colors)
# for i in range(0,n):
#     print("나는 %s을 좋아한다"%colors[i])

# animals=['코끼리','호랑이','사슴','펭귄','여우']
# i=0
# while i <len(animals):
#     print(animals[i])
#     i=i+1

# nameList=['a','b']
# noList = list(range[201001,241021])#에러
# print(noList)
# print(nameList[1])
# for i in noList:
#     print(i,end=" ")

# i=0
# while i < len(noList):
#     print( noList[i],end=" ")
#     i=i+1

# nameList=['이순신','홍길동','박수연']
# nameList[2]='박수현'
# for i in nameList:
#     print(i,end=" ")

# nameList.append('홍대길')
# for i in nameList:
#     print(i,end=" ")
# nameList.insert(1,"a")
# print()
# for i in nameList:
#     print(i,end=" ")
# try:
#     nameList=['박수현','이순신','홍길동','a','b']    
#     searchIdnex=nameList.index('박수현',0,10)
#     print(searchIdnex)
#     searchIdnex=nameList.index('장수현',0,10)
#     print(searchIdnex)
# except ValueError:
#     print(" 리스트에없습니다.")  
# 
# member=[1,2,1,2,3,4,3,1,2,3,4,4]
# member.remove(2)
# print(member)  

# member=[1,2,1,2,3,4,3,1,2,3,4,4]
# member.pop(2)
# print(member) 
# member.clear()
# print(member)

# person1=[1,2,3,4]
# person2=[5,6,7,8]
# person=person1 + person2
# print(person)

# p4=list(range(1,11))
# print(p4)
# sum=0
# for i in p4:
#     sum+=i
# print(sum)

# p5= [100,8,90]
# p5Sum=sum(p5)
# print(p5Sum)
# p5Avg=p5Sum/len(p5)
# print(p5Avg)
# p5Max=max(p5)
# print(p5Max)

# p6=['apple','banana','orarnge']
# print(p6)
# p6Copy=p6.copy
# print(p6Copy)
# p6.remove('apple')
# print(p6)
# p6Copy[2]='manggo'
# print(p6)

p7=['apple','banana','orange']
p77=p7
print(p7)
print(p77)
p7.remove('apple')

print(p7)
p7=['apple','banana','orange']
p77[1]='mango'
print(p7)
print(p77)

p7=['apple','banana','orange']
p77=p7
print(p7)
print(p77)