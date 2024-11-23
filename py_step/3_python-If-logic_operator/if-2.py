# print('짝수일까? 홀수일까? 내가 알아봐줄게 넣어봐!')
# num_value = int(input())

# if num_value % 2 == 0 :
#     print('짝수 입니다.')
# else : 
#     print('홀수 입니다.')


value = int(input())

if value <= 12 :
    print('탈 수 없습니다.')
elif value <= 15 :
    print('부분적으로 탈 수 있습니다.')
elif value <= 17 :
    print('자이로드롭을 제외하고 모두 가능')
if value :
    print('환영합니다.')
else :
    print('다 탈 수 있습니다.')