x = 0
y = 6001

while x < 10:
    x = int(input("Enter X: "))

while y > 6000:
    y = int(input("Enter Y: "))

def check(num):
	temp = num
	digit = 0
	while temp > 0: 
		digit = temp % 10;
		if digit == 0:
			return 0
		elif num % digit != 0:
			return 0
		elif temp > 9:
			temp /= 10
		else:
			return 1

for i in range(x, y + 1):
	if check(i) == 1:
		print(i)
