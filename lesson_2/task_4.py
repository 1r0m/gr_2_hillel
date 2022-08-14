year = int(input("Вкажіть рік який хочете перевірити : "))
if year % 4 == 0 and y % 100 != 0:
	print("YES")
elif y % 400 == 0:
	print("YES")
else :
	print("No")
