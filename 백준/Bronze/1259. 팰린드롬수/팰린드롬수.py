while True:
    num = input()
    if num == '0':
        break
    
    n = len(num)
    is_palindrome = True
    for i in range(n//2):
        if num[i] == num[n-i-1]:
            continue
        else:
            is_palindrome = False
            break
    
    if is_palindrome:
        print('yes')
    else:
        print('no')