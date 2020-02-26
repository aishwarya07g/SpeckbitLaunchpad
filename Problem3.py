num1 = eval(input("Enter a list: "))
num2 = []
for i in range(len(num1)):
	if num1[i]==2:
		num2.append(i)
print(num2)
