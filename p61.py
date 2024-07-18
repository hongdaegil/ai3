score=80
print('성적'+str(score))

x="토끼"*10
print(x)

n="100"*20
print(n)

n200=200
print(str(n200)*15)

date='20220301'
year=date[0:5-1]
month=date[4:6]
day=date[6:]
date2=year+'-'+month+'-'+day
print(date2)

#
x='수학성적:'
print(type(x))
y='80'
print(type(y))
z=x+str(y)
print(type(z))

x='가는 말이 고와야 오는 말이 곱다.'
n=len(x)
print('문자열의 길이:'+str(n))

x='홍대길'
print('홍대길'*3)

#퀴즈
x='말 한마디로 천냥 빛을 갚다'
print(len(x))

x='홍대길'
y='01099274243'
z=y[10]
print(z)
print('홍대길'*int(z))

phone1='82-10-8744-334'
phone2='82-02-123-45687'
phone3='010-9927-4243'


if len(phone3)==15: 
   print('한국 핸드폰 번호입니다.')
else :
   print('한국 집번호 입니다.')

if len(phone1)==15 and len(phone2)==15:
   print('phone1은 핸드폰 번호입니다.')
   print('phone1는 핸드폰 번호입니다.')
elif len(phone1)==14 and len(phone2)==14:
   print('phone1은 집 번호입니다.')
   print('phone2는 집 번호입니다.')
elif len(phone1)==15 and len(phone2)==14:
   print('phone1은 핸드폰 번호입니다.')
   print('phone2는 집 번호입니다.')
elif len(phone1)==14 and len(phone2)==15:
   print('phone1은 집 번호입니다.')
   print('phone2는 핸드폰 번호입니다.')

print("안녕하세요.\n만나서\t\t반갑습니다.")