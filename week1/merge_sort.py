#coding=utf8

def merge(left, right):
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
    return r

def merge_sort(l):
    length = len(l)
    if length == 1:
        return l
    left = merge_sort(l[:length/2])
    right = merge_sort(l[length/2:])
    return merge(left, right)


if __name__ == '__main__':
    print merge_sort([7,4,5,43,3,123,34,2,5,6,356,7,7])
