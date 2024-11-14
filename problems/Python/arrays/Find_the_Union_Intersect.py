def findUnion(a, b):
    i = 0
    j = 0
    union = []
    
    # Merge two sorted arrays while ensuring uniqueness
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if len(union) == 0 or union[-1] != a[i]:  # Avoid duplicates
                union.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if len(union) == 0 or union[-1] != b[j]:  # Avoid duplicates
                union.append(b[j])
            j += 1
        else:
            # a[i] == b[j], so add only one element
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
            j += 1
    
    # Add remaining elements from a, if any
    while i < len(a):
        if len(union) == 0 or union[-1] != a[i]:  # Avoid duplicates
            union.append(a[i])
        i += 1
    
    # Add remaining elements from b, if any
    while j < len(b):
        if len(union) == 0 or union[-1] != b[j]:  # Avoid duplicates
            union.append(b[j])
        j += 1
    
    return union


a = [1,2,3,4,5]
b = [1,2,3]

print(findUnion(a,b))


def findIntersection(a, b):
    i = 0
    j = 0

    intersect = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            intersect.append(a[i])
            i += 1
            j += 1
        elif a[i] >= b[j]:
            j += 1
        elif a[i] <= b[j]:
            i += 1
    
    return intersect


a = [1,2,3,4,5]
b = [1,2,3]

print(findIntersection(a,b))