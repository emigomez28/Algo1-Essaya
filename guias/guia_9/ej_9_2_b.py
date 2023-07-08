def carac_ocurrences(string):
    counts = dict()
    words = string.lower().split()
    for word in words:
        for carac in word:
            if carac in counts:
                counts[carac] += 1
            else:
                counts[carac] = 1
    return counts

s = "Que lindo dia hace hoy"
print(carac_ocurrences(s))