import random

def insertsort(a, i, j):
    for x in xrange(i+1, j):
        tmp = a[x]
        while x > i and tmp < a[x-1]:
            a[x] = a[x-1]
            x -= 1
        a[x] = tmp

def merge(a, i, m, j):
    l = []
    k1 = i
    k2 = m
    while k1 < m and k2 < j:
        if a[k1] < a[k2]:
            l.append(a[k1])
            k1 += 1
        else:
            l.append(a[k2])
            k2 += 1
    while k1 < m:
        l.append(a[k1])
        k1 += 1
    while k2 < j:
        l.append(a[k2])
        k2 += 1
    for x in xrange(i, j):
        a[x] = l[x-i]

def mergesort(a, i, j):
    if j - i <= 10:
        insertsort(a, i, j)
    else:
        m = (i+j)/2
        mergesort(a, i, m)
        mergesort(a, m, j)
        merge(a, i, m, j)

