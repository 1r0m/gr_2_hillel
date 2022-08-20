first_number = int(input("Вкажіть число:"))
second_number = int(input("Вкажіть наступне число:"))

if first_number < second_number:
	for i in range(first_number, second_number + 1, 1):
		print(i)

elif first_number > second_number:
	for i in range(second_number, first_number + 1, 1):
		print(i)



