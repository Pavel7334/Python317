import os

# Задание пути к корневой директории
root_directory = 'nested1'

# Получение списка файлов и директорий в корневой директории
all_entries = os.listdir(root_directory)

# Фильтрация записей для определения файлов и директорий
files = [entry for entry in all_entries if os.path.isfile(os.path.join(root_directory, entry))]
directories = [entry for entry in all_entries if os.path.isdir(os.path.join(root_directory, entry))]

# Вывод файлов
print("Files:")
for file in files:
    # Вывод полного пути к файлу
    print(os.path.join(root_directory, file))

# Вывод директорий
print("\nDirectories:")
for directory in directories:
    # Вывод полного пути к директории
    print(os.path.join(root_directory, directory))