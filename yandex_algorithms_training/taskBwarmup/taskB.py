import math

f = open("Coding/yandex_algorithms_training/taskBwarmup/f1.txt")
data = list(map(int, f.readline().split(" ")))
print(data)
upper = data[0] * data[3] + data[1] * data[2]
lower = data[1] * data[3]
cupper = upper
clower = lower
print(upper, lower)
while upper != 0 and lower != 0:
    if upper > lower:
        upper = upper % lower
    else:
        lower = lower % upper
divisor = lower + upper
print(math.floor(cupper / divisor), math.floor(clower / divisor))
