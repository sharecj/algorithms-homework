#coding=utf8

def quick_sort(num_list, pivot_index=0):
    # base condition
    if len(num_list) <= 1:
        return num_list, 0

    # choose pivot
    if pivot_index:
        num_list[0], num_list[pivot_index] = num_list[pivot_index], num_list[0]
    pivot = num_list[0]

    # partition
    i=1
    for j, num in enumerate(num_list[1:]):
        if num_list[j+1] < pivot:
            num_list[i], num_list[j+1] = num_list[j+1], num_list[i]
            i += 1
    num_list[0], num_list[i-1] = num_list[i-1], num_list[0]

    # recursion
    num_list[:i-1], left_cmp_count = quick_sort(num_list[:i-1])
    num_list[i:], right_cmp_count = quick_sort(num_list[i:])

    # count comparision count
    cmp_count = left_cmp_count + right_cmp_count + (len(num_list) - 1)

    return num_list, cmp_count


if __name__ == '__main__':
    f = open('QuickSort.txt', 'r')
    ints = f.readlines()
    ints = [int(i.strip()) for i in ints]
    print quick_sort(ints[:], 0)[1]
    print quick_sort(ints[:], -1)[1]
