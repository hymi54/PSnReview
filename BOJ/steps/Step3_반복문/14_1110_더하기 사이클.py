# temp = start = int(input())
# new = 10 * (start % 10) + (start // 10 + start % 10) % 10
# count = 1
#
# while new != start:
#     temp = new
#     new = 10 * (temp % 10) + (temp // 10 + temp % 10) % 10
#     count += 1
#
# print(count)

ini = int(input())
new = -1
count = 0

while ini != new:
    if new == -1:
        new = ini
    new = 10 * (new % 10) + (new // 10 + new % 10) % 10
    count += 1

print(count)
