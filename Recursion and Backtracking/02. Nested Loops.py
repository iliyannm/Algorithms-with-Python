def find_combo(idx, vector):
    if idx == len(vector):
        print(' '.join(str(x) for x in vector))
        return

    for i in range(1, len(vector) + 1):
        vector[idx] = i
        find_combo(idx + 1, vector)


n = int(input())
vector = []
for _ in range(n):
    vector = [None] * n

find_combo(0, vector)
