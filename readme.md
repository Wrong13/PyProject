Описание 
    Программа делит записи razb_uch.xlsx на две сущности
(выделенные цветов в самом файле) с колонки A до M и c N по V. Записывает их в фреймы и выводит. Подключается с pssql на локальной машине с паролем "password" и выбирает бд с именем "testbd". Создает эти две таблицы и делает в них перезапись.   

Инструкция по развертыванию

    1 Для активации виртуального окружения в прописать в консоль
        venv\Scripts\activate.bat - для Windows
        source venv/bin/activate - для Linux и MacOS
    2 Для установки зависимостей прописать 
        pip install -r requirements.txt
    3 Для запуска 
        python Pyproject.py

