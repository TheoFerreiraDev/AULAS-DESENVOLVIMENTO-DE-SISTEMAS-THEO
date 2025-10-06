    #Ex01
    def classificar_idade(self):
        self.assertEqual(classificar_idade(10), 'Criança')
        self.assertEqual(classificar_idade(15), 'Adolescente')
        self.assertEqual(classificar_idade(34), 'Adulto')
        self.assertEqual(classificar_idade(150), 'idade Invalida')       


    #Ex02
    def maiorMenor(self):
        self.assertEqual(maiorNumero(10, 5), 'O primeiro número é maior que o segundo número')
        self.assertEqual(maiorNumero(5, 10), 'O segundo número é maior que o primeiro número')
        self.assertEqual(maiorNumero(7, 7), 'Os dois são iguais')
 

    #Ex03
     def VogalConsoante(self):
         self.assertEqual(vogalConsoante('a'), 'A letra que você digitou é uma vogal')
         self.assertEqual(vogalConsoante('b'), 'A letra que você digitou é uma consoante')    
         self.assertEqual(vogalConsoante('z'), 'A letra que você digitou é uma consoante')
         self.assertEqual(vogalConsoante('e'), 'A letra que você digitou é uma vogal')        

    #Ex04
    def SenhaIgual(self):
        self.assertEqual(senhaIgual('1234','1234'), 'Acesso permitido')
        self.assertEqual(senhaIgual('1234','4321'), 'Acesso negado')    
        self.assertEqual(senhaIgual('abcd','abcd'), 'Acesso permitido')
        self.assertEqual(senhaIgual('abcd','abdc'), 'Acesso negado')

    #Ex05
    def passado(self):
        self.assertEqual(passado(8,7,9), 'Aprovado')
        self.assertEqual(passado(5,6,4), 'Reprovado')    
        self.assertEqual(passado(7,7,7), 'Aprovado')
        self.assertEqual(passado(3,2,1), 'Reprovado')
    
    #Ex06
    def reverse(self):
        self.assertEqual(reverse(1,2,3), [3,2,1])
        self.assertEqual(reverse(10,20,30), [30,20,10])    
        self.assertEqual(reverse(-1,-2,-3), [-3,-2,-1])
        self.assertEqual(reverse(0,0,0), [0,0,0])
        
    #Ex07
    def consumo(self):
        self.assertEqual(consumo(2, 60), 30.0)
        self.assertEqual(consumo(1.5, 80), 26.67)
        self.assertEqual(consumo(3, 100), 33.33)
        self.assertEqual(consumo(0, 50), 0.0)
