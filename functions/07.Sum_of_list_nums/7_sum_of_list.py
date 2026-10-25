def list_sum(n):
    total=0
    for i in range(0,len(n)):
        total=total+n[i]
    return total
print(list_sum([1,2,3,4]))