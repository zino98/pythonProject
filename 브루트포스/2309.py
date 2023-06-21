import sys

array = []
for _ in range(9):
    array.append(int(sys.stdin.readline()))

total = sum(array)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if (total - array[i] - array[j]) == 100:
            one = array[i]
            two = array[j]
            break

array.remove(one)
array.remove(two)
array.sort()

for height in array:
    print(height)