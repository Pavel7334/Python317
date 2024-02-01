print(f"Все призёры: ['Natalia', 'Maxim', 'Evgeniya', 'Alexandr', 'Matvei', 'Michail']")
winners_mathematics = {'Natalia', 'Maxim', 'Evgeniya', 'Matvei', 'Michail'}
winners_physics = {'Maxim', 'Matvei', 'Alexandr'}
print(f"Призеры обеих команд: {winners_mathematics & winners_physics}")
print(f"Обновленный список призеров по математике: {winners_mathematics - (winners_physics ^ winners_mathematics)}")

