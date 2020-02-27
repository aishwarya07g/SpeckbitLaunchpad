str = input("Enter String: ")

str1 = str.split(" ")
str1 = str1[-1::-1]
str2= " ".join(str1)

if __name__ == "__main__": 
	print(str2)