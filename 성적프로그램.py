
name=[]
kor=[]
eng=[]
mat=[]
menu='1'
while menu !='5':
    print('-------------------')
    print('성적관리 프로그램')
    print('-------------------')
    print('1.학생이름 입력하기')
    print('2.성적 입력하기')
    print('3.통계자로 보기')
    print('4.학생 자료 삭제하기')
    print('5.프로그램 종료하기')
    menu=input('====>메뉴를 선택하세요(1/2/3/4/5)')
    if menu=='1':
        n=input("학생 이름은?")# 학생이름 입력하기??
        name.append(n)
        print(name)#지울것
    elif menu=='2':
        try:
            k=int(input("국어점수는?"))
            e=int(input("영어점수는?"))
            m=int(input("수학점수는?"))#성적 입력하기??
            kor.append(k)
            eng.append(e)
            mat.append(m)
            print(kor,eng,mat)
        except ValueError:
            print("점수를 입력해 주셔야 합니다.")     
    elif menu=='3':
        print('1번) 반 성적 검색')
        print('2번) 개인점수 검색')        
        stMenu=input('번호를 선택해서 나가기(1/2)')#통계 입력하기
        if stMenu == '1':
            print()
            print('-------------------------')
            print('이름 국어 영어 수학')
            print('-------------------------')
            for i in range(len(name)):
                print('%s %d %d %d'%(name[i],kor[i],eng[i],mat[i]))#반전체 통계
        elif stMenu=='2':
            sName=input('점수를 알고 싶은 학생이름은?')
            try:
                sIndex=name.index(sName)
                print("%s %d %d %d"%(name[sIndex],kor[sIndex],eng[sIndex],mat[sIndex]))  
            except ValueError:
                 print("%s 우리반 학생이 아닙니다."%sName)
            # okName=-1
            # for i in range(len(name)):
            #     if sName==name[i]:
            #         okName=i
            # if okName==-1:
            #     print('%s우리반 학생이 아닙니다'%sName)
            # else:
            #     print("%s %d %d %d"%(name[sIndex],kor[sIndex],eng[sIndex],mat[sIndex]))                            
    elif menu=='4':
        #학생자료 입력하기
       delName=input("삭제하려는 학생의 이름은?")
       try:
           sIndex=name.index(delName)
           name.pop(sIndex)
           kor.pop(sIndex)
           eng.pop(sIndex)
           mat.pop(sIndex)
       except ValueError:
           print("%s 우리반 학생이 아니야"%delName)


    else: menu=='5'
        #프로그램 종료

# 검색 프로그램 find
#          sName=input('점수를 알고 싶은 학생이름은?')
# sIndex=name.find(sName)
#             okName=-1
#             for i in range(len(name)):
#                 if sName==name[i]:
#                     okName=i
#             if okName==-1:
#                 print('%s우리반 학생이 아닙니다'%sName)
#             else:
#                 print("%s %d %d %d"%(name[okName],kor[okName],eng[okName],mat[okName]))