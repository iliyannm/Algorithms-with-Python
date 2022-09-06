def generate_vector(idx, vector):
    if idx == len(vector):
        print(''.join(str(x) for x in vector))
        return

    for num in range(2):
        vector[idx] = num
        generate_vector(idx + 1, vector)


n = int(input())
vector = [None] * n

generate_vector(0, vector)
