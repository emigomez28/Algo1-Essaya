def max_and_pos(list):
    max = 0
    pos = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            pos = i
    return max, pos

l = [1,2,3,4,6,78,90,8970,0,9000]
l2 = [" ","asd","emi","alfa","beta","aaa231465"]
print(max_and_pos(l))
#print(max_and_pos(l2))