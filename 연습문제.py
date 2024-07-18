a=input("시작 수를 입력하세요:")
b=input("끝 수를 입력하세요:")
x=31
for i in range(2,x):
    if x%i==0:
        print("%d소수가 아니다:"%x)
        break
    if x==i+1:
        print("%d소수다"%x)