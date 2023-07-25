import random

def radix_sort(num_list):
    t = 0
    while 10 ** t <= max(num_list):
        buckets = [[] for i in range (10)]
        for num in num_list:
            ordering_digit = (num // 10 ** t) % 10
            buckets[ordering_digit].append(num)
        num_list.clear()
        for bucket in buckets:
            num_list.extend(bucket)
        t += 1  

test_list = list(range(1000))
random.shuffle(test_list)
print(test_list)
radix_sort(test_list)
print(test_list)
