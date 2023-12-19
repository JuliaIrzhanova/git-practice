def create_task(title, description):
   #Логика создания задачи 
    print(f"Создана новая задача: {title}")

    # Добавляем функционал управления задачами
    task = Task(title, description)
    task.save()
    print("Задача сохранена")
