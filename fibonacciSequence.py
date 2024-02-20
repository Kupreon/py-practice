size = int(input("How many numbers of the Fibonacci sequence do you want to print out? "))

num = [0 for i in range(0, size)]
num[0] = 0
num[1] = 1

print(num[0])
print(num[1])

for i in range(2, size):
    num[i] = num[i - 2] + num [i - 1]
    print(num[i])
