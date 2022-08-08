a, b, c = map(int, input().split())
product = 0

if c <= b:
    print('-1')
else:
    """
    첫 번째 풀이
    """
    # while a + b*product >= c*product:
    #     product += 1
    # print(product)

    """
    두 번째 풀이
    """
    print(a//(c-b)+1)
