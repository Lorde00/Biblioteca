import time
import sys

def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

rej = 'Romeu & Julieta'
pp = 'Pequeno Príncipe'
om = 'Os Miseráveis'
ddaf = 'Diário de Anne Frank'
oovs = 'O Ódio que Você Semeia'
abdi = 'A Barca do Inferno'
ber = 'Berserk Vol 43'
vaga = 'Vagabound Vol 4'
ds = 'Demons Slayer Vol 3'
ble = 'Bleach Vol 2'


livros = [{'Nome': 'Romeu & Julieta', 'Autor': 'William Shakespeare', 'Ano': 1597, 'Identificação': 298436},
        {'Nome': 'Pequeno Príncipe', 'Autor': 'Antoine de Saint-Exupéry', 'Ano': 1943, 'Identificação': 387640},
        {'Nome': 'Os Miseráveis', 'Autor': 'Victor Hugo', 'Ano': 1862, 'Identificação': 152873},
        {'Nome': 'Diário de Anne Frank', 'Autor': 'Anne Frank', 'Ano': 1947, 'Identificação': 743901},
        {'Nome': 'O Ódio que Você Semeia', 'Autor': 'Angie Thomas', 'Ano': 2017, 'Identificação': 539872},
        {'Nome': 'A Barca do Inferno', 'Autor': 'Gil Vicente', 'Ano': 1517, 'Identificação': 623009},
        {'Nome': 'Berserk Vol 43', 'Autor': 'Kentaro Miura', 'Ano': 1988, 'Identificação': 529187},
        {'Nome': 'Vagabound Vol 4', 'Autor': 'Takehiko Inoue', 'Ano': 1998, 'Identificação': 726192 },
        {'Nome': 'Demon Slayer Vol 3', 'Autor': 'Koyoharu Gotouge', 'Ano': '2016', 'Identificação': 864001},
        {'Nome': 'Bleach Vol 2', 'Autor': 'Tite Kubo', 'Ano': 2001, 'Identificação': 928371}]



def catalogo():
    for livro in livros:
        for chave, valor in livro.items():
                print(f' {chave}: {valor} ')
        print()
    
    while True:
        empsn = str(input('Deseja pegar algum livro emprestado [S/N]?\n ')).upper()
        match empsn:
            case 'N':
                return 'Voltando ao menu inicial... '
            case 'S':
                escolha = str(input('Qual dos livros você deseja pegar emprestado?\n'))
                match escolha:
                    
                    
                    case 'Romeu & Julieta':
                        slowPrint('Este livro está emprestado para Julia Krauss / Dia de devolução: 05/01/2024\n',0.1)
                    
                    
                    case 'Pequeno Príncipe':
                        slowPrint('Este livro está emprestado para Pedro Barbosa / Dia de devolução: 15/01/2024\n',0.1)
                    
                    
                    case 'Os Miseráveis':
                        slowPrint('Este livro está emprestado para Louise Plemb / Dia de devolução: 17/12/2023\n',0.1)    
                    
                    
                    case 'Diário de Anne Frank':
                        slowPrint('Este livro está disponível\n',0.1)
                        escolha2 = str(input('Deseja pegar este livro emprestado [S/N]?\n ')).upper()
                        if livro_usuario == []:
                            livro_usuario.append(escolha) 
                            return f'Parabéns, você pegou {ddaf}, você tem até o dia 22/01/2024 para devolver!!\n'       
                        else:
                            return f'Devolva o {livro_usuario} primeiro para pegar outro livro!\n '                                   
                    
                    
                    case 'O Ódio que Você Semeia':
                        slowPrint('Este livro está disponível\n',0.1)
                        escolha2 = str(input('Deseja pegar este livro emprestado [S/N]?\n ')).upper()   
                        if escolha2 == 'S':
                            if livro_usuario == []:
                                livro_usuario.append(escolha)   
                                return f'Parabéns, você pegou {oovs}, você tem até o dia 24/01/2024 para devolver!\n'
                            else:
                                return f'Devolva o {livro_usuario} primeiro para pegar outro livro!\n '        
                    
                    
                    case 'A Barca do Inferno':
                        slowPrint('Este livro está emprestado para Pedro Alberga / Dia de devolução: 15/12/2023\n',0.1)
                    
                    
                    case 'Berserk Vol 43':
                        slowPrint('Este livro está disponível\n',0.1)
                        escolha2 = str(input('Deseja pegar este livro emprestado [S/N]?\n ')).upper()    
                        if escolha2 == 'S':          
                            if livro_usuario == []:
                                livro_usuario.append(escolha)   
                                return f'Parabéns, você pegou {ber}, você tem até o dia 18/01/2024 para devolver!\n'
                            else:
                                return f'Devolva o {livro_usuario} primeiro para pegar outro livro!\n'    
                    
                    
                    case 'Vagabound Vol 4':
                        slowPrint('Este livro está emprestado para Kaio Nilago / Dia de devolução: 29/12/2023\n',0.1) 
                    
                    
                    case 'Demon Slayer Vol 3':
                        slowPrint('Este livro está disponível\n',0.1)
                        escolha2 = str(input('Deseja pegar este livro emprestado [S/N]?\n')).upper()    
                        if escolha2 == 'S':          
                            if livro_usuario == []:
                                livro_usuario.append(escolha)   
                                return f'Parabéns, você pegou {ds}, você tem até o dia 19/01/2024 para devolver!\n'
                            else:
                                return f'Devolva o {livro_usuario} primeiro para pegar outro livro!\n'    
                    
                    
                    case 'Bleach Vol 2':
                        slowPrint('Este livro está disponível\n',0.1)
                        escolha2 = str(input('Deseja pegar este livro emprestado [S/N]?\n ')).upper()    
                        if escolha2 == 'S':          
                            if livro_usuario == []:
                                livro_usuario.append(escolha)                
                                return f'Parabéns, você pegou {ble}, você tem até o dia 28/01/2024 para devolver!\n '
                            else:
                                return f'Devolva o {livro_usuario} primeiro para pegar outro livro!\n'                       


def retorno():
    decisao2 = str(input(f'{nome} você está com o livro {livro_usuario} em mãos, gostaria de devolve-lo [S/N]?\n ')).upper()
    match decisao2:
        case 'S':
            livro_usuario.clear()
            return f'Parabéns você devolveu o {livro_usuario}! Retornando ao menu...\n'
                    
                
          
n = []
livro_usuario = []
nome = str(input('Digite seu nome para acessar as opções!\n '))
n.append(nome)
n.append(livro_usuario)

while True:
    print('1: Catálago\n' '2: Devolver livro\n' '3: Sair\n')
    print(n)
    decisao = float(input(f'Bem vindo(a) {nome}! Qual opção você deseja escolher [1/2/3]?\n'))
    match decisao:
        case 1:
            print(catalogo())
        
        case 2:
            print(retorno())
        
        case 3:
            print(f'Obrigado por visitar a biblioteca {nome}! Volte sempre!\n')
            break
        
        
            
            
    
    
       
       

    
        
    
    
    