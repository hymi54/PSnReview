# group_count = 0
#
# for _ in range(int(input())):
#     s = input()
#     s_len = len(s)
#     diff = 1
#
#     # 불연속점 찾기
#     for i in range(s_len - 1):
#         if s[i] != s[i+1]:
#             diff += 1
#
#     if len(set(s)) == diff:
#         group_count += 1
#
# print(group_count)

result = 0
for i in range(int(input())):
    word = input()
    print(sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
