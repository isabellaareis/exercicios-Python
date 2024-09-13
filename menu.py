from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n-------MENU-------\n\n' +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair' +
              '\n1. Somar' +
              '\n2. Subtrair' +
              '\n3. Dividir' +
              '\n4. Multiplicar' +
              '\n5. Potência' +
              '\n6. Raiz' +
              '\n7. Tabuada' +
              '\n8.exercicio 1' +
              '\n9.exercicio 2' +
              '\n10.exercicio 3' +
              '\n11.exercicio 4' +
              '\n12.exercicio 5' +
              '\n13.exercicio 6' +
              '\n14.exercicio 8' +
              '\n15.exercicio 9' +
              '\n16.exercicio 10' +
              '\n17.exercicio 11' +
              '\n18.exercicio 12' +
              '\n19.exercicio 13' +
              '\n20.exercicio 14' +
              '\n21.exercicio 15' +
              '\n22.exercicio 16'+
              '\n23.exercicio 17'+
              '\n24.exercicio 18'+
              '\n25.exercicio 19'+
              '\n26.exercicio 20'
              )

    def coletar(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))

    def coletar1(self):
        self.num1 = int(input("Informe o número: "))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print('\nObrigado.')

            if self.opcao == 1:
                self.coletar()
                print(f'\nA soma dos números é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()
                print(f'\nA subtração dos números é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'\nA divisão dos números é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'\nA multiplicação dos números é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'\nO resultado da potência é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz do {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'\nA raiz do {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif (self.opcao == 8):
                print(self.opera.exercicio1())

            elif (self.opcao == 9):
                print(self.opera.exercicio2())

            elif (self.opcao == 10):
                print(self.opera.exercicio3())

            elif (self.opcao == 11):
                print(self.opera.exercicio4())

            elif self.opcao == 12:
                self.coletar1()
                print(f'\no número {self.num1} é: {self.opera.exercicio5(self.num1)}')

            elif self.opcao == 13:
                self.coletar1()
                print(f'\no número {self.num1} é: {self.opera.exercicio6(self.num1)}')

            elif (self.opcao == 14):
                self.coletar1()
                print(f'\n {self.opera.exercicio8(self.num1)}\n')

            elif (self.opcao == 15):
                self.coletar1()
                print(f'\n {self.opera.exercicio9(self.num1)}\n')

            elif (self.opcao == 16):
                print(self.opera.exercicio10())

            elif (self.opcao == 17):
                self.coletar1()
                print(f'\n {self.opera.exercicio11(self.num1)}\n')

            elif (self.opcao == 18):
                self.coletar1()
                print(f'O fatorial do número {self.num1} é: \n{self.opera.exercicio12(self.num1)}\n')

            elif (self.opcao == 19):
                print(self.opera.exercicio13())

            elif (self.opcao == 20):
                self.coletar1()
                print(f'\n{self.opera.exercicio14(self.num1)}\n')


            elif (self.opcao == 21):
                self.coletar1()
                print(f'\n A soma dos digitos do número {self.num1} é: {self.opera.exercicio15(self.num1)}\n')

            elif (self.opcao == 22):
                self.coletar1()
                print(f'\n{self.opera.exercicio16(self.num1)}\n')

            elif self.opcao == 23:
                self.coletar1()
                print(f'\n  {self.opera.exercicio17(self.num1)}')



            elif (self.opcao == 24):
                self.coletar1()
                print(f'A sequência de Collatz do número {self.num1} é: \n{self.opera.exercicio18(self.num1)}\n')

            elif (self.opcao == 25):
                self.coletar1()
                print(f'\n{self.opera.exercicio19(self.num1)}\n')

            elif (self.opcao == 26):
                self.coletar1()
                print(f'\n{self.opera.exercicio20(self.num1)}\n')






            else:
                print("Código escolhido não é válido!")





