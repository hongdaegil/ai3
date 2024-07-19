# data=[12,8,15,35,-3,-20,15,34,6]
# print(data)
# data.sort()
# print(data)

# data2=['a,','가','힝','1','나']
# print(data2)
# data2.sort()
# print(data2)
# data2.sort(reverse=True)#내림차순으로 나오게하기
# print(data2)
# data2.sort(reverse=False)#뒤집기
# print(data2)

# string1='사과는 맛있다. 나는 사과를 제일 좋아한다'
# print(string1)
# x=string1.replace("사과","딸기"-1)
# string1=[x]                  
# print(string1)

# hello= "have-a-nice-day"
# print(hello)

# list1=hello.split(" ")
# print(list1)
# print(type(list1))

# for i in range(0,len(list1)):
#     print("list1[%d]:%s"%(i,list1[i]))

# ab='a,b,c,d,e,f'
# print(ab)
# list1=ab.split(' ')
# print(list1)
# list2=ab.split((','))
# print(type(list2))

# for i in range(0,len(list2)):
#     print("list1[%d]:%s"%(i,list2[i]))


# ab=['홍길동:100:20','이순신:90:90','최수연:100:75']
# print(ab)
# list1=ab.split(' ')
# print(list1)
# list2=ab.split((':')) #해결하기
# print(type(list2))

# for i in range(0,len(list2)):
#     print("list1[%d]:%s"%(i,list2[i]))


# list2=['홍길동:100:20','이순신:90:90','최수연:100:75']
# list22=[]
# for i in list2:
#     list10= i.split(':')
#     print(list10)
#     for j in list10:
#         list22.append(j)
    
# print(list22)

# list = []
# list5 = ['kbs-사장-200,mbc-부장-100','kbs-사원-50,sbs-대리-80']
# for i in list5 :
#     list_5 = i.split('-')
#     print(list_5)
#     for j in list_5 :
#         list__5 = j.split(',')
#         print(list__5)
#         for k in list__5 :
#             list.append(k)
#             print(list)


#------------------------------------
#데이터를 사이트에서 가져오기
# import requests as req
# url="https://search.naver.com/search.naver"
# rData=req.get(url,params={"query":'백일해 증상'})
# print(rData.text)

# names=['황에린','홍지수','안지영']
# print(names)
# x='*'.join(names)
# print(x)

# phone1=['010','1234','5678']
# print(phone1)
# x='-'.join(phone1)
# print(x)
# numbers=[[1,2],[3,4,5],[1]]#
# print(numbers[])#

# #####list2DD=[[1,2,3,4],[5,6,7]]
# print( len(list2DD))
# print( len(list2DD[0]))
# print( len(list2DD[1]))
# for i in range(0,len(list2DD)):
#     for j in range(0,len(list2DD[i])):
#         print(list2DD[i][j],end=" ")
#     print()
# print(numbers[1][2])
# for i in range(0,1):
#     for j in range(0,3):
        
#         print("numbers[%d][%d]=%d"%(i,j))


#3차원
list3D=([[1,2,3],[4,5]],[[6,7],[8]])
print(list3D[0][0][0])