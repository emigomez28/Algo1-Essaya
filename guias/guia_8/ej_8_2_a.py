def max_value(list):
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    print(max)
    return max

l = [1,2,3,4,6,78,90,8970,0,9000]
max_value(l)