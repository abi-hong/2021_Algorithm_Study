number = int(input())
hansu = 0

for i in range(1, number + 1):
    if (i < 100):
        hansu += 1
    else:
        number_list = list(map(int, str(i)))
        # str(i) : 숫자를 문자열로 만들어준다.
        # map(int, str(i)) : 문자열로 되어있는 각 자릿수를 정수로 바꿔준다.
        # (ex, "123" > 정수 1, 2, 3 각각으로 바꿔준다.)
        # 즉, 리스트의 모든 요소를 int를 사용해서 변환
        # list함수로 list로 변환한다.
        if(number_list[0] - number_list[1] == number_list[1] - number_list[2]):
            hansu += 1
print(hansu)
