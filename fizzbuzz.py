"""
Criar um programa "fizz buzz" que escreva na tela os números
inteiros de 1 a 100, fazendo as seguintes substituições:
Fizz, se os números fores divisíveis por 3;
Buzz, se os números fores divisíveis por 5;
Fizzbuzz, se os números fores divisíveis por 15;
"""
for i in range(1, 101):
    # Visto que os números divisíveis por 15 também o são por 5,
    # o teste condicional por 15 será executado primeiro.
    if i % 15 == 0:
        print('\033[1;37;40m fizz-buzz \033[m')
    elif i % 5 == 0:
        print('\033[1;30;42m buzz \033[m', end=' ')
    elif i % 3 == 0:
        print('\033[1;30;43m fizz \033[m', end=' ')
    else:
        if i < 10:  # Inserir um zero à esquerda de números com apenas um algarismo a fim de manter tudo alinhado.
            print(f'0{i}', end=' ')
        else:
            print(i, end=' ')
