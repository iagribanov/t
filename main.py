import csv
with open('students_new.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"') #Создает объект reader, читающий CSV-файл и интерпретирующий строки как словари.
    data = sorted(reader, key=lambda x: x['titleProject_id']) #Сортирует данные из CSV по значению 'titleProject_id' и сохраняет результат в переменной data.
id_project = input() #Запрашивает у пользователя ввод и сохраняет значение в переменной id_project.
while (id_project != 'СТОП'): #Запускает цикл, который выполняется до тех пор, пока ввод пользователя не 'СТОП'.

    id_project = int(id_project) #Преобразует введенное значение в целое число.
    for el in data: #Начинает цикл, перебирающий элементы списка data.
        if int(el['titleProject_id']) == id_project: #Проверяет, соответствует ли 'titleProject_id' текущего элемента введенному пользователем id проекта.
            surname, name, patronymic =  el["Name"].split() #Разделяет полное имя на фамилию, имя и отчество.
            print(f"Проект No{id_project} делал: {name[0]}. {surname} он(а)получил(а) оценку - {el['score']}.") #Выводит информацию о студенте
            break
    else: #Если цикл завершается без прерывания (break), выполняется блок кода, выводящий сообщение о том, что ничего не найдено.
        print('Ничего не найдено')
    id_project = input() #Запрапользователя новый ввод и обновляет переменную id_project
