def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
                
        if count == 0:
            average = 0
        else:
            average = total / count
        return total, average
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка в даних файлу.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("path/to/salary_file.txt")
if total is not 0 and average is not 0:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
