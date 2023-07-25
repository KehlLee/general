import random

def sift(num_list, low, high):
    i = low
    j = i * 2 + 1 # j设为左孩子
    tmp = num_list[low]
    while j <= high:
        if j + 1 <= high and num_list[j] < num_list[j+1]: # <小根堆, >大根堆
            j += 1
        if tmp < num_list[j]: # <小根堆, >大根堆
            num_list[i] = num_list[j]
            i = j
            j = i * 2 + 1
        else:
            num_list[i] = tmp # 放在孩子都比tmp小的根节点
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
    print(num_list)


# heap_sort([1, 2, 3, 4])
test_list = list(range(50))
random.shuffle(test_list)
print(test_list)
heap_sort(test_list)
