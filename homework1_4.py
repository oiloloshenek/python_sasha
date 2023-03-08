#Определение функции для переворота строки
def flip_over(string):
	st = []
	fr = []
	#Перебирает строку и добавляет в список
	for strings in string:
		st.append(strings)
	
	#Вытягивает из списка st последнее значение и добавляет 
	#в список fr
	while st:
		fr.append(st.pop())
		
	#Убирает все  лишние знаки и выводит на экран
	#отформатированный вывод	
	result = ''.join(fr)	
	print(result)
		
flip_over(string = input("Введите строку: "))
