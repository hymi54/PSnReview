"""
풀이 1 : list.reverse()
"""
a, b = map(list, input().split())
a.reverse()
b.reverse()
a = int(''.join(a))
b = int(''.join(b))

print(max(a, b))

"""
풀이 2 : 슬라이싱으로 뒤집기
"""

# a = a[::-1]
# b = b[::-1]
#
# print(max(a, b))

"""
풀이 3 : 파이써닉한 방법
"""

# print(max(a[::-1], b[::-1]))
