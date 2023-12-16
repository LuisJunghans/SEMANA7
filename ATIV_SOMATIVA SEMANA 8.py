# Luis Felipe Bandeira Junghans - Análise e Desenvolvimento de Sistemas

# Modularização do menu principal, menu de operações, inclusão de estudantes,
# listagem de estudantes, edição de estudantes e exclusão de estudantes.

import json

estudantes = []
professores = {}
disciplinas = {}
turmas = {}
matriculas = {}

# criada a def para abrir o arquivo json

def arquivo_json(data, registros_academicos):
     with open(registros_academicos + '.json', 'w') as f:
        json.dump(data, f)

# abaixo seguem as defs de menu e suas opções para a escolha do usuário

def excluir_aluno():
    nome = input('Escreva o nome de um estudante para excluir: ')
    if nome in estudantes:
          estudantes.remove(nome)
          print('Estudante excluído com sucesso.')
    else :
          print('Estudante não encontrado.')

def menu_principal():
    print('========== MENU PRINCIPAL ========== \n\n')
    print('1. Estudantes.')
    print('2. Professores.')
    print('3. Disciplinas.')
    print('4. Turmas.')
    print('5. Matrículas.')
    print('0. Sair.\n\n\n')

def menu_estudantes():
            print('\n\n ========== MENU DOS ESTUDANTES ========== \n\n')
            print('1. Incluir.')
            print('2. Listar.')
            print('3. Atualizar.')
            print('4. Excluir.')
            print('0. Voltar ao menu principal.\n\n\n')

def adicionar_aluno():
    addestudante = input('Nome do Estudante: ')
    estudantes.append(addestudante)
    print('Adicionado com êxito!\n\n')

def listar_aluno():
    if len (estudantes) == 0:
        print('Não há registros até o momento.\n\n')
    else:
        print('Segue a lista dos estudantes: ')
        for estudante in estudantes:
          print(estudante,'\n')

def cod_estudante():
     ce = int(input('Insira o código do estudante: '))
     estudantes[ce] = 'Código do Estudante'

def atualizar_estudantes():
     estudante = input('Digite o nome de um estudante para atualizar: ')
     if estudante in estudantes:
          estudantes.remove(estudante)
          adicionar_aluno()
          print('Estudante atualizado com sucesso!')

def menu_professores():
     print('========== Professores ==========\n')
     print('1. Código do professor. ')
     print('2. Nome do professor. ')
     print('3. CPF do professor. ')
     print('0. Voltar.\n\n')
     
def cod_prof():
     cp = int(input('Insira o código do professor: '))
     professores[cp] = 'Código do professor'

def nome_prof():
     nomeprof = input('Insira o nome do professor: ')
     professores[nomeprof] = 'Nome'

def cpf_prof():
     cpfprof = input('Insira o CPF do professor: ')
     professores[cpfprof] = 'CPF'

def materias():
     print('========== Matéria ==========\n')
     print('1. Código da matéria.')
     print('2. Nome da matéria.')
     print('0. Voltar.\n\n')

def cod_disciplina():
     cd = int(input('Insira o código da disciplina: '))
     disciplinas[cd] = 'Código da Disciplina'

def nome_disciplina():
     nd = input('Insira o nome da disciplina: ')
     disciplinas[nd] = 'Número da disciplina'

def turma():
     print('========== Turmas ==========\n')
     print('1. Código da turma.')
     print('2. Código do professor.')
     print('3. Código da disciplina.')
     print('0. Voltar.\n\n')

def codigo_turma():
     cod_turma = int(input('Insira o código da turma: '))
     turmas[cod_turma] = 'Código da turma'

def matricula():
     print('========== Matrícula ==========\n')
     print('1. Código da turma.')
     print('2. Código do estudante.')
     print('0. Voltar.\n\n')

# abaixo seguem as opções dos menus e seus comandos referenciados pelas funçoes acima, onde ele se repete até ser tomada uma decisão pelo usuário

while True:
    menu_principal()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        while True:
            menu_estudantes()
            opcao2 = input('Escolha um opção: ')
            if opcao2 == '1':
                 adicionar_aluno()
            elif opcao2 == '2':
                 listar_aluno()
            elif opcao2 == '3':
                 atualizar_estudantes()
            elif opcao2	== '4':
                 excluir_aluno()
            elif opcao2 == '0':
                 break
    elif opcao == '2':
         while True:
              menu_professores()
              opcao3 = input('Escolha uma opção: ')
              if opcao3 == '1':
                cod_prof()
              elif opcao3 == '2':
                   nome_prof()
              elif opcao3 == '3':
                   cpf_prof()
              elif opcao3 == '0':
                   break
    elif opcao == '3':
        while True:
             materias()
             opcao4 = input('Escolha uma opção: ')
             if opcao4 == '1':
                  cod_disciplina()
             elif opcao4 == '2':
                  nome_disciplina()
             elif opcao4 == '0':
                  break
    elif opcao == '4':
        while True:
             turma()
             opcao5 = input('Escolha uma opção: ')
             if opcao5 == '1':
                  codigo_turma()
             elif opcao5 == '2':
                  cod_prof()
             elif opcao5 == '3':
                  cod_disciplina
             elif opcao5 == '0':
                  break
    elif opcao == '5':
        while True:
             matricula()
             opcao6 = input('Escolha uma opção: ')
             if opcao6 == '1':
                  codigo_turma()
             elif opcao6 == '2':
                  cod_estudante()
             elif opcao6 == '0':
                  break
    elif opcao == '0':
        print('Finalizando sistema...')
        break
    

# aqui são os arquivos json onde serão armazenados os dados inseridos pelo usuário no sistema
    
arquivo_json(professores, 'registro_professores')
arquivo_json(disciplinas, 'registro_disciplinas')
arquivo_json(turmas, 'registro_turmas')
arquivo_json(matriculas, 'registro_matriculas')
arquivo_json(estudantes, 'registro_estudantes')