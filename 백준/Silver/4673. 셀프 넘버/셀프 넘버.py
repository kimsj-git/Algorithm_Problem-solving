def next_num(num1):
    num2 = num1
    for i in str(num1):
        num2 += int(i)
    return num2

def nums_created(num):
    set_created = set()
    while num <= 10000:
        # num의 다음 수(num과 각 자리수의 합)를
        # set_created에 추가
        set_created.add(next_num(num))
        # 다음 수를 num에 저장
        num = next_num(num)
    return set_created

final_set = set()
for i in range(1, 10000):
    if i not in final_set:
        final_set = final_set | nums_created(i)


num_set = {i for i in range(1, 10001)}

self_num = num_set - final_set

final_list = sorted(list(self_num))
for i in final_list:
    print(i)
