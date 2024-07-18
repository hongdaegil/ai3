print('낮은 수 부터 높은 수로 가능합니다.')
x = int(input('시작 : '))
y = int(input('끝 : '))
z = int(input('원하는 배수 : '))
cnt = int(input('종료를 원하는 배수의 갯수(0입력시 건너뛰기) : '))
sum2 = int(input('종료를 원하는 수(초과의 경우 종료, 0입력시 건너뛰기) : '))
sum3 = int(input('종료를 원하는 배수의 합계(0입력 시 종료) : '))

sum = 0
count = 0
if x > sum2 and x > y:
    print('시작값보다 낮은 수로 종료할 수 없습니다.')
else :
    print('숫자 나열 :', end=' ')
    if y >= 0 :
        if x < y :
            if x < z:
                a = x%z
                b = x+z-a
                num = b
                for i in range(b,y+1,z) :
                    sum = sum + i
                    print(num , end=', ')
                    num = num + z
                    count += 1
                    if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                        break
            elif x == z :
                num= x
                for i in range(x,y+1,z) :
                    sum = sum + i
                    print(num , end=', ')
                    num = num + z
                    count += 1
                    if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                        break
            elif x > z :
                a = x%z
                b = x-a+z
                num = b
                for i in range(b,y+1,z) :
                    sum = sum + i
                    print(num , end=', ')
                    num = num + z
                    count += 1   
                    if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                        break
        elif x > y :
            if x < z:
                a = x%z
                b = x-a
                num = b
                for i in range(b,y+1,z) :
                    sum = sum + i
                    print(num , end=', ')
                    num = num + z
                    count += 1
                    if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                        break
            elif x > z :
                a = x%z
                b = x-a
                num = b
                for i in range(b,y,-z) :
                    sum = sum + i
                    print(num , end=', ')
                    num = num - z
                    count += 1   
                    if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                        break

    elif y < 0 :
        for i in range(x,y-1,-z) :
            a = x%z
            b = x-a+z
            num = b
            sum = sum + i
            if i != 0 :
                print(i, end=', ')
                count += 1
            else :
                count = count
            if count == cnt or sum2 != 0 and sum2 < num or sum3 != 0 and sum >= sum3:
                break
    ave = sum/count
    if sum3 == 0 and cnt == 0 and sum2 == 0 :
        print()
        print('종료사유 : 없음')
    elif cnt == count :
        print()
        print('종료 사유 : 배수의 갯수 초과')
    elif sum2 < y :
        print()
        print('종료 사유 : 마지막 수 초과')
    elif sum3 < sum:
        print()
        print('종료 사유 : 배수의 합계 초과')

    if num >= 0 :  
        print()
        print('%d부터 %d까지의 %d의 배수의 마지막 수 : %d'%(x,y,z,num-z))
        print('%d부터 %d까지의 %d의 배수의 갯수 : %d'%(x,y,z,count))
        print('%d부터 %d까지의 %d의 배수의 합계 : %d'%(x,y,z,sum))
        print('%d부터 %d까지의 %d의 배수의 평균 : %.2f'%(x,y,z,ave))
    else :
        print()
        print('%d부터 %d까지의 %d의 배수의 마지막 수 : %d'%(x,y,z,-(num-z)))
        print('%d부터 %d까지의 %d의 배수의 갯수 : %d'%(x,y,z,count))
        print('%d부터 %d까지의 %d의 배수의 합계 : %d'%(x,y,z,sum))
        print('%d부터 %d까지의 %d의 배수의 평균 : %.2f'%(x,y,z,ave))