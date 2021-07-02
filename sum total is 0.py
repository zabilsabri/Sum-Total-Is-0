n = [-1, 0, 1, 2, -1, -4]
p = len(n)

for i in range(p-2):
    for j in range(i+1, p-1):
        for k in range(j+1, p):
            if n[i] + n[j] + n[k] == 0:
                print(n[i], n[j], n[k])