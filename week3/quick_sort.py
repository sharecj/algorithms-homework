#coding=utf8

def get_first_element_as_pivot(l):
    return 0, l[0]

def get_last_element_as_pivot(l):
    return -1, l[-1]

def get_median_of_three_as_pivot(l):
    pos = [0, len(l) / 2 + (len(l) % 2) - 1, -1]
    mapping = {l[p]:p for p in pos}
    val = mapping.keys()
    val.remove(min(val))
    median = min(val)
    return mapping[median], median

def quick_sort(num_list, choose_pivot_func):
    # base condition
    if len(num_list) <= 1:
        return num_list, 0

    # choose pivot
    pivot_index = choose_pivot_func(num_list)[0]
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
    num_list[:i-1], left_cmp_count = quick_sort(num_list[:i-1], choose_pivot_func)
    num_list[i:], right_cmp_count = quick_sort(num_list[i:], choose_pivot_func)

    # count comparision count
    cmp_count = left_cmp_count + right_cmp_count + (len(num_list) - 1)

    return num_list, cmp_count


if __name__ == '__main__':
    f = open('QuickSort.txt', 'r')
    ints = f.readlines()
    ints = [int(i.strip()) for i in ints]
    print quick_sort(ints[:], get_first_element_as_pivot)[1]
    print quick_sort(ints[:], get_last_element_as_pivot)[1]
    print quick_sort(ints[:], get_median_of_three_as_pivot)[1]
