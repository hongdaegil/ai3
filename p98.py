# x=-10
# if x > 0 :
#    print("양수")
#    print("조건이 참일때 수행")
# print("조건문 배워요")

# y=80
# if y >= 90 :
#     print("A+")
# else:
#     print("낮은 점수")
# print("모두 실행되는곳")

# a=8
# b=10
# if a>=b :
#     print("a가더크다")
# else:
#     print("b가더크다")
# print("판단끝")

# csorc=int(input("점수는"))
# if csorc>=90 :
#     print("A입니다")
# elif csorc>=80:
#     print("B입니다")
# elif csorc>=70:
#     print("c입니다")
# elif csorc<=69:
#     print("f입니다")
# print("끝")

# score1=75
# score2=90
# print(score1>=80 and score2>=80)

# score1=85
# score2=95
# print(score1>=80 or score2>=95)

# x=10
# print(x%2==0 or x%6==0)

# a=5
# b=7
# c=a+b
# print(c==12)

# age=int(input("나이는?"))
# ticket=2000
# if age>=65:
#     ticket=0
#     print("나이:%d세"%age)
#     print("입장료:%d원"%ticket)
# print(age)

age=int(input("나이는"))
ticket=2000
if age>=10 and age<=20 :
    ticket=1500
    print("나이%d세"%age,"입장료는%d원"%ticket)
elif age>=5 and age<=9:
    ticket=1200
    print("나이%d세"%age,"입장료%d원"%ticket)
elif age>=0 and age<=4:
    ticket=1000
    print("나이%d세"%age,"입장료%d원"%ticket)
print("어서오세요")

