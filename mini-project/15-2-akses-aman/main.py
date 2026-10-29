def get(data, size, index):
    if index < 0 or index >= size:
        raise IndexError(f"index {index} di luar 0..{size - 1}")
    return data[index]

data = [7, 9, 4, 0, 0]
size = 3
for i in [1, 3, -1]:
    try:
        print(f"get({i}) =", get(data, size, i))
    except IndexError as e:
        print("Error:", e)
