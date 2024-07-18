# start=int(input("시작"))
# end=int(input("끝"))
# num=int(input("정수를 입력하세요"))
# result="%d은%d~%d사이에 없다"%(num,start,end)
# if start>=200 and end<=500:
#     result="%d는 %d~%d사이에있다"%(num,start,end)
#     print(result)

month=input("월을 숫자로입력하세요")
if month=="3" or month== "4" or month== "5":
    print("%s월은 봄입니다"%month)
elif month=="6"or month=="7"or month=="8":
    print("%s월은 여름입니다"%month)
elif month=="9"or month=="10"or month=="11":
    print("%s월은 가을입니다"%month)
elif month=="12"or month=="1" or month=="2":
    print("%s월은 겨울입니다"%month)

# len=123456-12789123
# a=int(input("주민번호를 입력해주세요:"))
# if a==1 or a==3:
#     print("%s는남성입니다"%a)
# if a==2 or a==4:
#     print("%s는 여성입니다."%a)
