liczby = [5, 2, 1, 4, 3]

for i in range(len(liczby)):
    i_min = i
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[i_min]:
            i_min = j
    liczby[i], liczby[i_min] = liczby[i_min], liczby[i]

print(liczby)