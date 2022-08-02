import time

start_time = time.time()
# for i in range(1, int(input()) + 1):
#     print(i)
print('\n'.join(map(str, range(1, int(input())+1))))
consume_time = time.time() - start_time
print(consume_time)
