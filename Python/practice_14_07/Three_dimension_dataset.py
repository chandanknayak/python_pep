def input_3d(layers, rows, cols):
    data = []

    for i in range(layers):
        print(f"Enter Layer {i+1}")
        layer = []

        for j in range(rows):
            row = list(map(int, input().split()))
            layer.append(row)

        data.append(layer)

    return data


def add_3d(data1, data2):
    result = []

    for i in range(len(data1)):
        layer = []
        for j in range(len(data1[i])):
            row = []
            for k in range(len(data1[i][j])):
                row.append(data1[i][j][k] + data2[i][j][k])
            layer.append(row)
        result.append(layer)

    return result


layers = int(input("Layers: "))
rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("Enter First 3D Array")
A = input_3d(layers, rows, cols)

print("Enter Second 3D Array")
B = input_3d(layers, rows, cols)

print("Result:")
print(add_3d(A, B))