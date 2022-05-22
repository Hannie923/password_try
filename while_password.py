while True:
	password = input ('請輸入密碼：')
	if password != 'a123456':
		print ('密碼錯誤！ 還有3次機會')
	password2 = input ('請輸入密碼：')
	if password2 != 'a123456':
		print ('密碼錯誤！ 還有2次機會')
	password3 = input ('請輸入密碼：')
	if password3 != 'a123456':
		print ('密碼錯誤！ 還有1次機會')
	password4 = input ('請輸入密碼：')	
	if password4 != 'a123456':
		break	
	else : 
		print ('登入成功')	
		break
