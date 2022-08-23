print("Converter Arábico para Romano - Digite 1 \nConverter Romano para Arábico - Digite 2\n")
opcao = input("Digite sua opção: ")

if opcao == "1":
    x = int(input("Escreva um número inteiro: "))

    def int_romano(x):
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12
        roman_numeral = ''
        while x != 0:
            if numbers[i] <= x:
                roman_numeral += roman[i]
                x = x - numbers[i]
            else:
                i -= 1
        return roman_numeral
    print(int_romano(x))

elif opcao == "2":
    y = input("Escreva o número romano: ").upper()

else:
    print("ERRO \n TENTE NOVAMENTE.")
