file = open("input.txt")


def find_element(arr, l, r):
    min_value = min(arr[l : r + 1])
    for i in range(l, r + 1):
        if arr[i] != min_value:
            return arr[i]
    return "NOT FOUND"


n, m = (file.readline()).strip("\n").split(" ")
sequence = (file.readline().strip("\n")).split(" ")
seq = list(map(int, sequence))


for _ in range(eval(m)):
    length, queries = (file.readline()).strip("\n").split(" ")
    result = find_element(seq, eval(length), eval(queries))
    print(result)
