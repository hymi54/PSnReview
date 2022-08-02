n, x = map(int, input().split())
'''
풀이 1
'''
# arr = map(int, input().split())
# for i in arr:
#     if i < x:
#         print(i, end=' ')

'''
풀이 2
'''
arr = [i for i in map(int, input().split()) if i < x]
print(' '.join(map(str, arr)))
