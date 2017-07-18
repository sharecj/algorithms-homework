#coding=utf8

def merge(left, right):
    inversion_count = 0
    r = []
    i = 0
    j = 0
    len_left = len(left)
    len_right = len(right)
    length = len_left + len_right
    for k in range(length):
        if j >= len_right:
            r.append(left[i])
            i+=1
        elif i >= len_left:
            r.append(right[j])
            j+=1
        elif left[i] <= right[j]:
            r.append(left[i])
            i+=1
        else:
            r.append(right[j])
            j+=1
            inversion_count += (len_left - i)
    return r, inversion_count

def merge_sort(l):
    length = len(l)
    if length == 1:
        return l, 0
    left, left_inversion = merge_sort(l[:length/2])
    right, right_inversion = merge_sort(l[length/2:])
    total, cross_inversion = merge(left, right)
    return total, left_inversion + right_inversion + cross_inversion


if __name__ == '__main__':
    f = open('IntegerArray.txt', 'r')
    ints = f.readlines()
    ints = [int(i.strip()) for i in ints]
    print merge_sort(ints)[1]
