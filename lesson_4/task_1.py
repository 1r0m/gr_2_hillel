first_number = int(input("Вкажіть кільксть кілометрів за перший день:"))
number_day = int(input("Вкажіть відстань яку пробіг спортсмен:"))
c = 1

while first_number < number_day :
	first_number = first_number * 1.1
	c = c + 1 
	print(c)
