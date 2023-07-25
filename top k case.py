import random
# 小根堆建堆
def sift(num_list, low, high):
    i = low
    j = i * 2 + 1 # j设为左孩子
    tmp = num_list[low]
    while j <= high:
        if j + 1 <= high and num_list[j] < num_list[j+1]:
            j += 1
        if tmp < num_list[j]:
            num_list[i] = num_list[j]
            i = j
            j = i * 2 + 1
        else:
            num_list[i] = tmp # 放在孩子都比tmp大的根节点
            break
    else:
        num_list[i] = tmp # 放在最后的叶子节点

def heap_sort(num_list):
    n = len(num_list)
    for i in range((n-2)//2, -1, -1):
        # print(i)
        sift(num_list, i, n-1)
    for j in range(n-1, -1, -1):
        num_list[0], num_list[j] = num_list[j], num_list[0]
        sift(num_list, 0, j-1)

test_list = list(range(50))
random.shuffle(test_list)
print(test_list)
heap_sort(test_list)
print(test_list)

k = int(input('Please type in k:'))
max_list = test_list[:k]
heap_sort(max_list)
for i in range(k, len(test_list)):
    if test_list[i] > max_list[0]:
        test_list[i], max_list[0] = max_list[0], test_list[i]   
        heap_sort(max_list)
print(max_list)