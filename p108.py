# num=int(input("양의정수를입력하세요"))
# result="다음기회에"
# if num%2 ==0:
#     result="행운의수"
# if num%4==0:
#     result="행운의수"
# if num%2==0 and num%4==0:
#     result="행운의수"
# print("%d은%s"%(num,result))

# unm=int(input("숫자를입력하세요"))

# if unm%2==0 and unm%4==0:
#     a="행운의수"
# else:
#     a=unm
# print(a)
  
start=int(input("시작"))
end=int(input("끝"))
num=int(input("정수를 입력하세요"))
result="%d은%d~%d사이에 없다"%(num,start,end)
if start>=200 and end<=500:
    result="%d는 %d~%d사이에있다"%(num,start,end)
    print(result)