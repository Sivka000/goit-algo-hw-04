def get_cats_info(path):
    cats = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)
                
        return cats
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except ValueError:
        print("Помилка в даних файлу." 
              "\nПереконайтеся, що кожен рядок містить три значення які розділені комами.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
