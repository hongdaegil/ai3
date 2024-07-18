s='안녕하세요, 반갑습니다.'
print(s)
print(s[0])
print(s[1:11])
print(s[8])
print(s[0],s[1])
print(s[0]+s[1])
print(s[0:2])
print(s[7:10])

s="쥐 구멍에 볕들 날있다."
print(s[2:8])

animal="tiger"
print(animal[0:2])

#응용
jumin="991013-2012456"
print(jumin[0:2]+'년'+jumin[2:4]+'월'+jumin[4:6]+'일')

sex=jumin[7]
print(sex)
 
#if-만약에
if sex==1 or sex==3 :
    print('남자')
else:
    print('여자')

#1단계 주민번호 제일 마지막 부분을 가지고 온다 응용
end = jumin[13]
print(end)
#2단계 문자6을 연산하기 위해서 숫자 6으로 형변환
endint=int(end)
#3단계 조건은 주민번호 오류 검출하기
if endint % 2 == 0:
    print('맞는 주민번호')
else: 
    print('틀린 주민번호')