import functools
import heapq

# Додавання чисел до списка 
list_number = []

while True: 
	element = input("Вкажіть число:")

	if element == "0":
		break

	if not element.isdigit():
		continue

	list_number.append(int(element))

# Довжина списка
len_of_list = len(list_number)
print(f"Довжина списка {len_of_list}")

# Пошук суми та добутку чисел
total_sum = 0
total_product = 1


for number in list_number:
	total_sum += number
	total_product *= number	
print(f"Сума чисел:{total_sum}")
print(f"Добуток чисел:{total_product}")

# Середнє Арифметичне
arithmetic_mean = sum(list_number)/len(list_number)
print(f"Середнє арифметичне {arithmetic_mean}")

# Максимальне число в списку
max_list_number = max(list_number)
index = list_number.index(max_list_number)
print(f"Максимальне значення:{max_list_number}\nПослідовність:{index + 1}")

# Пошук парних та не парних чисел
list_pair = []
list_not_pair = []

for numbers in list_number:
	if numbers % 2 == 0:
		list_pair.append(numbers)
print(f"Парні числа:{list_pair}")

for numbers in list_number:
	if numbers % 2 != 0:
		list_not_pair.append(numbers)
print(f"Не парні числа:{list_not_pair}")


second_element_value = heapq.nlargest(2, set(list_number))[1]
print(f"Другий елемент за значенням: {second_element_value}")

number_maximum_numbers = list_number.count(max_list_number)
print(f"Кількість чисел які дорівнюють максимальному числу: {number_maximum_numbers}")
