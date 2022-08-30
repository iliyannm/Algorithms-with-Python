def generate_vector(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        generate_vector(idx + 1, vector)


n = int(input())
vector = [0] * n
generate_vector(0, vector)
