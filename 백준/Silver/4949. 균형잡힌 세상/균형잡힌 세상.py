while True:
    line = input()
    if line == '.':
        break
    
    stack = []
    flag = False
    for char in line:
        if char in ['(', '[']:
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                print('no')
                flag = True
                break
        elif char == ']':
            if not stack or stack.pop() != '[':
                print('no')
                flag = True
                break
    if flag:
        continue

    if stack:
        print('no')
    else:
        print('yes')