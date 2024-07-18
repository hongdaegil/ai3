#20부터 50까지 나오게 만들기
# cnt=0
# sum=0
# for i in range(20, 51, 2):
#     print(i, end= " ")
#     cnt=cnt
#     sum=sum+i
# print("20~50까지의 2개씩 증가 숫자 갯수 %d"%cnt)
# print("20~50까지의 2개씩 증가의 숫자 합계 %d"%sum)

# word=input("영어 문장을 입력하세요:")
# for x in word:
#     print(x)

# phon=input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요:")
# for x in phon:
#     if x !="-":
#         print("%s"%x,end="")

# cnt=0
# for i in range(100,-1,-5):
#     print(i,end=" ")
# cot=cnt
# print("%d"%cnt)


# cnt=0
# sum=0
# for i in range(100,-1,-5):
#     cnt+=1
#     sum+=1
# print()
# print("100~0까지의 -5개씩 감소 숫자 갯수%d"%cnt)
# print("100~0까지의 -5개씩 감수 숫자의 합계%d"%sum)
# print("100~0까지의 -5개씩 감수 숫자의 평군%d"%int(sum//cnt))

#1부터 100까지의 합을 구하고 400에서 멈추기
# cnt=0
# sum=0
# for i in range(1,101,1):
#     if sum>=400:
#         print("합계가 400넘는 순간 i값은%d"%i)
#         break
#     sum+=i
# print("1~100까지 합%d"%sum)

#200~500까지 3개가 증가하는 수를 출력하기
#갯수가 20개일때 멈추기
# cnt=0
# sum=0
# for i in range(200,501,3):
#     print(i,end="")
#     cnt+=1
#     if cnt== 20:
#         break
# print()
# print("20개일때 i값%d"%i)
# cnt=0
# sum=0
# for i in range(5,501,5):
#     print(i,end=" ")
#     cnt+=1
#     sum+=i
#     if sum>=1000 or cnt>=30:
#         break
# print()
# print("합계가 1000이상 갯수가 30개 이상일때 머무기 멈추는값:%d %d %d"%(i,cnt,sum))

# c=

# print("-"*30)
# print("섭씨 화씨")
# print("-"*30)
# for i in range(-20,30,5):
#     f=c*9.0/5.0+32.5

#     print("%5d %6d.1"%(c,f))
# print("-"*30)

# count=0
# phone="01099274243"
# print(phone)
# for i in phone:
#     if i==5:
#         print("있어요")
#         count+=1
# if count==0:
#         print("없어요")

# flag=0
# phone="01099274243"
# print(phone)
# for i in phone:
#     if i==4:
#         flag=1
#         print("있어요")

# if flag==0:
#         print("없어요")

#응용
# z=0
# word=input("영어 문장을 입력하세요:")
# flag = 0
# for x in word:
#     if x=="a":
#         z+=1
#         flag = 1
# if flag == 0 :
#     print("없어요")    
# else :
#     print("%d 개 있어요"%z)    

# word = "apple"
# word='alppy'
# cnt = word.count("a")
# ans = False
# for i in word:
#     if i == "a":
#         ans = True 
#         print("%d개 있어요" %cnt)
#         break
# else:
#     print("없습니다")

#키보드로 입력을 받는다
# hp=input("핸드폰번호를 입력해주세요") 
# #한글자씩 가져와서 숫자를 배교한다
# for i in hp:
#     #숫자이면 출력한다 아니면 다시 2단계로 간다 #유니코드를 활용한다
#     #if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):#숫자판정 
#     if '가'<=i<='힣':#한글판정 한글유니코드
#         print('%s'%i,end="")


