v = int(input("Вкажіть швидкість Васі (км/год) : "))
t = int(input("Вкажіть час маршруту Васі (год.) : "))
s = v * abs(t)
if v > 0 and s <= 100 : 
	print("Вася рухається у позитивному напрямку за маршрутом")
	print(f"Вася зупинився на відмітці в  {s} кілометрів.")
if v < 0 and s <= 100 :
	s = v * t
	print(f"Вася затримався на відмітці в  {abs(s)} кілометрів. Поспішайте!")
else:
	print("Ви закінчили!")

