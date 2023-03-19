					Программа "ГЕНЕРАТОР ТЕСТОВ"

_________________________________________________________________________________________

Программа для генерации вариантов самостоятельных в форматах pdf, txt, docx по темам:

	* Арифметическиен операции в различных системах счисления
	
	* Перевод между системами счисления с основаниями 2, 4, 8, 16

Пользователю доступны такие настройки работы как:

	* Выбор темы самостоятельной работы

	* Выбор количества вариантов, которые необходимо сгенерировать

	* Выбор количества заданий в каждом варианте

	* Выбор формата итогового файла

	* Выбор папки, в которую необходимо сохранить сгенерированные файлы.


Для сохранения параметров уже сгенерированных работ и, соответственно, возможности сгенерировать 
работу повторно, предусмотрено создание аккаунта и вход в свой аккаунт. В приложении присутствует 
база данных, в которую сохраняются параметры каждый сгенерированный работы для конкретного 
пользователя.


_________________________________________________________________________________________


					СТАРТОВОЕ ОКНО

На стартовом окне пользователю предлагается войти в аккаунт или зарегистрироваться. Кнопки 
"Войти в аккаунт" и "Зарегистрироваться" кликабельны и ведут на соответствующие окна приложения. 
Надпись снизу нефункциональна и присутствует лишь для более взвешенного дизайна, чтобы убрать
пустоту в нижней части окна.


_________________________________________________________________________________________

					ВОЙТИ В АККАУНТ

Окно предназначено для входа в аккаунт под своим логином и паролем. Приложении сообщит пользователю, 
если пользователя, с введённым им логином не существует, или, если пароль не подходит к данному 
логину. Кнопка войти в аккаунт в случае правильно введённых данных переводит пользователя на окно с 
главным меню. Надпись "Восстановить пароль" опять же присутствует для дизайна.

Все пароли, конечно же, шифруются, но если Вам не хочется создавать новый аккаунт, то Вы можете 
воспользоваться стандартным аккаунтом, на котором уже создан ряд работ. Логин: "test", пароль: "123".


_________________________________________________________________________________________

					ОКНО ВЫБОРА РОЛИ

Предполагалось, что при выборе одной из ролей пользователь будет получать слегка различный функционал,
но на данный момент данная фича не реализована и выбор роли не имеет значения для дальнейшего 
использования приложения пользователем. Тем не менее, данное окно позволяет мне продемонстрировать, 
что я научился добавлять картинки в PyQt. Впрочем, это было не сложно :)


_________________________________________________________________________________________

					ОКНО РЕГИСТРАЦИИ

Окно предоставляет пользователю возможность создать новый аккаунт. Приложение сообщит, если пользователь
с таким логином уже существует, или, если введённые пароли не совпадают. В случае успешно пройденной
регистрации пользователя переводят на экран входа в приложении. А надпись "вернуться в главное меню"
опять же про дизайн.



_________________________________________________________________________________________

					ГЛАВНОЕ МЕНЮ

Кнопка "Создать тест" переводит пользователя на страницу для настройки параметров нового теста. 
Кнопка "Созданные тесты" переводит пользователя на окно с таблицей, в которой будут отображены все
тесты, которые он создавал ранее. Кнопка "Выход" вызывает диалоговое окно с вопрсоом точно ли пользователь
хочет выйти из приложения и в случае положительного ответа окно приложения закрывается.



_________________________________________________________________________________________

					ОКНО СОЗДАНИЯ НОВОГО ТЕСТА

Все функции, доступные пользователю при создании теста уже были перечислены выше. При нажатии на кнопку
"Сгенерировать" в выбранной пользователем папке генерируются работы с заданными параметрами (при генерации сразу
болшого количества вариантов в формате pdf возможно временное зависание программы). При нажатии на кнопку
"Отмена" пользователю снова откроется главное меню.



_________________________________________________________________________________________

					ОКНО СОЗДАННЫХ РАНЕЕ ТЕСТОВ

На данном окне пользователь может выбрать в таблице строку с одним из ранее сгенерированных файлов и
изменить её настройки или сгенерировать работу по данным параметрам повторно. Должна быть выбрана ровно одна строка,
если строки не будут выбраны или будет выбрано несколько строк, программа предупредит об этом пользователя выведя 
соответствующее диалоговое окно. Также недопускается выделение нескольких ячеек строки, а не всей строки целиком.
Кнопка "Назад" возвращает пользователя в главное меню приложения. Нажатие на кнопку "редактировать" открывает диалоговое
окно с настройкой некоторых параметров работы, которые затем пользователь может перезаписать в базе данных. 
Нажатие на кнопку "Сгенерировать" сгенерирует выбранную работу повторно.



_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________

					УСТАНОВКА И ЗАПУСК

1. Распаковать архив.
2. Установить все библиотеки из файла requirements.txt
3. Запустить программу.
*4. Возможно потребуется исправить пути к файлам базы данных и картинкам проекта


Кроме того, при помощи библиотеки auto-py-to-exe был сгенерирован .exe файл программы, он также находится 
в архиве. В exe файле не работает генерация файлов в формат .pdf.

