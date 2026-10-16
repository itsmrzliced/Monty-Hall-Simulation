import random 
import matplotlib.pyplot as plt

print("Monty Hall Game Simulation")

runs = 100000
correct = 0
wrong = 0

for i in range(runs):
    car_door = random.randint(1, 3)
    player_door = random.randint(1, 3)
    doors = [1, 2, 3]

    goat_doors = []
    for i in range(3):
        if (i + 1) != car_door:
            goat_doors.append(i + 1)
            
    for i in goat_doors:
        if player_door != i:
            doors.remove(i)
            break
    
    for i in doors:
        if player_door != i:
            player_door = i
            break

    if player_door == car_door:
        correct += 1
    else:
        wrong += 1

percentage = runs / 100
correct_percentage = correct / percentage
wrong_percentage = wrong / percentage
x_axis = ["Correct", "Wrong"]
y_axis = [correct_percentage, wrong_percentage]
plt.bar(x_axis, y_axis)
plt.title("Monty Hall Simulation")
plt.xlabel("Choice")
plt.ylabel("Percentage")
plt.show()
