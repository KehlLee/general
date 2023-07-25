import random
def partition(num_list, left, right):
    temp = num_list[left]
    while left < right:
        while left < right and num_list[right] >= temp:
            right -= 1
        num_list[left] = num_list[right]
        while left < right and num_list[left] <= temp:
            left += 1
        num_list[right] = num_list[left]
    num_list[left] = temp
    return left
#     print(num_list, left, right)


def quick_sort(info, left, right):
    if left < right:
        mid = partition(info, left, right)
        quick_sort(info, left, mid-1)
        quick_sort(info, mid+1, right)

test_list = list(range(50))
random.shuffle(test_list)
print(test_list)
quick_sort(test_list, 0, len(test_list)-1)
print(test_list)
