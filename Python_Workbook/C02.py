input_degree = int(input('water degree?'))

if input_degree<0 : print('Wrong!')
elif input_degree<25 : print('Cool Water')
elif input_degree<40 : print('Water')
elif input_degree<80 : print('Hot Water')
else : print('So Hot! Don\'t touch!')
