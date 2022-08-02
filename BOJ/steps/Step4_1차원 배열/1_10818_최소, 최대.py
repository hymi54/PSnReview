input()
arr = list(map(int, input().split()))

# 풀이 1 : min(), max() 사용
print(min(arr), max(arr))

# 풀이 2 : 직접 비교해서 찾기
min_num = max_num = arr[0]

for i in arr:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(min_num, max_num)
