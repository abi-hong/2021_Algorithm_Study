#(x, y)
N = int(input())
num_list = []

for i in range(N):
    x, y = map(int, input().split())  # 입력받은 값을 공백을 기준으로 분리
    num_list.append((x, y))

for c in num_list:
    rank = 1

    for n in num_list:
        if(c[0] != n[0]) & (c[1] != n[1]):
            if(c[0] < n[0]) & (c[1] < n[1]):
                rank += 1
    print(rank)
