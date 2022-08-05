"""
풀이 1 : c, d, l, n, s, z가 있을 때 뒤 문자 체크
"""
s = input()
s_len = len(s)
count = i = 0

while i < s_len:
    try:
        match s[i]:
            case 'c':
                if s[i+1] == '=':
                    i += 1
                elif s[i+1] == '-':
                    i += 1
            case 'd':
                if s[i+1] == 'z':
                    if s[i+2] == '=':
                        i += 2
                elif s[i+1] == '-':
                    i += 1
            case 'l':
                if s[i+1] == 'j':
                    i += 1
            case 'n':
                if s[i+1] == 'j':
                    i += 1
            case 's':
                if s[i+1] == '=':
                    i += 1
            case 'z':
                if s[i+1] == '=':
                    i += 1
        count += 1
        i += 1
    except IndexError:
        count += 1
        break

print(count)
