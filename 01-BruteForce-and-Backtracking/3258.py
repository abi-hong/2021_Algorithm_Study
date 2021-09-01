N, Z, M = map(int, input().split())
s = input().split()
x = map(int, s)  # 리스트 s에 들어감

# 원형인거 생각하자!!
for k in range(1, Z):
    result = 1
    while (1):
        result = (result + k) % N
        if (result == 0):
            result = N
        if (result in s) or (result == 1):
            break
        if (result == Z):
            print(k)
            break
    if(result == Z):
        break
