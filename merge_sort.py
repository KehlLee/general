import random
def merge(num_list, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if num_list[i] < num_list[j]:
            tmp.append(num_list[i])
            i += 1
        else:
            tmp.append(num_list[j])
            j += 1
    else:
        if i > mid and j <= high:
            tmp += num_list[j:high+1]
        if j > high and i <= mid:
            tmp += num_list[i:mid+1]
    num_list[low:high+1] = tmp

def merge_sort(num_list, low, high):
    if low < high:
        mid = (high + low) // 2
        merge_sort(num_list, low, mid)
        merge_sort(num_list, mid+1, high)
        merge(num_list, low, mid, high)

test_list = list(range(50))
random.shuffle(test_list)
print(test_list)
merge_sort(test_list, 0, len(test_list)-1)
print(test_list)
