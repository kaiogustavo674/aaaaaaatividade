print ('projeto fitness!!')
while True:
    print("O que você quer fazer ?")
    option= input('"Logar","Cadastrar-se"')
    if option == "Logar":
        gmail =input("Digite seu gmail")
        senha =input("digite sua senha")
    elif option == "Cadastrar-se":
        cadastro = input("Qual o seu gmail")
        if cadastro != gmail:
            print("gmail incorreto")
            cadastro2 = input("Qual sua senha")
            if cadastro2 != senha:
                print("senha incorreta")
while True:
 print('tela inicial')
 opcao = int (input('digite a opção que você deseja escolher (1: peso ideal, 2:, 3:  '))
 
 if opcao == (1):
  print('peso ideal')
  input("Qual a sua altura")
    
