
# 이중 for문을 사용하여 하트를 여러 줄에 출력하기 - 줄과 하트 수 입력받기

a = int(input('하트를 몇 줄 출력할까요? : '))   # 가변 이중 loop 입력을 받아서 
b = int(input('출력할 하트 수를 입력하세요 : '))

for i in range(1,a+1) :
    print()
    for j in range(1, b+1) :
        print('♥', end = '')