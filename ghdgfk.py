

graf1 = [

    [0, 4, 0, 0, 7, 2, 0],  # A

    [4, 0, 1, 8, 8, 0, 0],  # B

    [0, 1, 0, 0, 0, 3, 0],  # C

    [0, 8, 0, 0, 13, 16, 0],  # D

    [7, 8, 0, 13, 0, 0, 0],  # E

    [2, 0, 3, 16, 0, 0, 1],  # F

    [0, 0, 0, 0, 0, 1, 0]  # M

]



print("1. Матрица смежности:")

for row in graf1:
    print(row)





num_vertices = len(graf1)

print(f"2. Количество вершин: {num_vertices}")





count_degree_3 = 0

for i in range(num_vertices):

    degree = 0

    for j in range(num_vertices):

        if graf1[i][j] > 0:
            degree += 1

    if degree == 3:
        count_degree_3 += 1

print(f"3. Количество вершин со степенью 3: {count_degree_3}")





num_edges = 0

for i in range(num_vertices):

    for j in range(i + 1, num_vertices):

        if graf1[i][j] > 0:
            num_edges += 1

print(f"4. Количество ребер: {num_edges}")





sum_of_weights = 0

for i in range(num_vertices):

    for j in range(i + 1, num_vertices):
        sum_of_weights += graf1[i][j]

print(f"5. Сумма весов всех ребер: {sum_of_weights}")







vertex_F_index = 5

neighbor_count_F = 0

for j in range(num_vertices):

    if graf1[vertex_F_index][j] > 0:
        neighbor_count_F += 1

print(f"6. Количество соседних вершин F: {neighbor_count_F}")



