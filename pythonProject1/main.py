HEIGHT = 182
WEIGHT = 75
STEPS = 20250
TIME = 55

def calories_calc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

def distance_calc(h,s):
	return (((h/4 + 0.37) * s)/100)/1000

calories = calories_calc(HEIGHT,WEIGHT,STEPS,TIME)
print(f"Калорий сожжено: {calories}")
# Калорий сожжено: 879.71

distance = distance_calc(HEIGHT,STEPS)
print(f"Дистанция в км: {distance}")
# Дистанция в км: 7.03


if distance > 4:
	print("Дистанция больше 4 км")
elif distance > 2:
	print("Дистанция больше 2 км")
else:
	print("Дистанция меньше 2 км")
# Дистанция больше 4 км


