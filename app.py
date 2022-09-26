from ast import arg
from contextlib import nullcontext
import sqlite3
from winreg import QueryValue

#criando banco de dados, caso não exista
conn = sqlite3.connect('agenda.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        tel TEXT
);
""")

print('Tabela criada com sucesso.')

def visualizar():
    seleciona = "SELECT tel FROM contatos"
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    if len(resultado) == 0:  #Verifica se o retorno contém alguma linha
        print('\nAgenda vazia\n')
    else:
        cursor.execute("""SELECT * FROM contatos""")
        for row in cursor:
            print(f'\n Nome: \n {row[1]} \n Telefone: \n {row[3]} \n E-mail: \n {row[2]} \n')

        print('\n[1] VOLTAR AO MENU PRINCIPAL')
        print('[2] EXIT\n')
        resp = int(input('Qual opcao? '))
        if(resp == 1):
            main()
        elif(resp == 2):
            exit()

def addcontato():
    telin = input('Digite o telefone com DDD. ex: 21988776655: ')
    nomein = input('Digite o nome do contato: ')
    emailin = input('Digite o email do contato: ')
    if telin == '' or nomein == '' or emailin == '':
        print('\nNenhum campo pode estar vazio\n')
        addcontato()
        
    seleciona = "SELECT tel FROM contatos WHERE tel ='{}'".format(telin)
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    if len(resultado) != 0:  #Verifica se o retorno contém alguma linha
        print('\nTelefone Já Cadastrado\n')
        addcontato()
    else:
        cursor.execute("""INSERT INTO contatos (tel, nome, email) VALUES (?, ?, ?)""", (telin, nomein, emailin))
        conn.commit()
        print('\nCadastro realizado\n')
        visualizar()

def editar():
    seleciona = "SELECT tel FROM contatos"
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    if len(resultado) == 0:  #Verifica se o retorno contém alguma linha
        print('\nAgenda vazia\n')
    else:
        cursor.execute("""SELECT * FROM contatos""")
        for row in cursor:
            print(f'\n Nome: \n {row[1]} \n Telefone: \n {row[3]} \n E-mail: \n {row[2]} \n')

        print('\n[1] VOLTAR AO MENU PRINCIPAL')
        print('[2] EXIT\n')
        resp = int(input('Qual opcao? '))
        if(resp == 1):
            main()
        elif(resp == 2):
            exit()

def main():
    while True:
        print('\n')
        print('=' * 15)
        print('MENU INTERATIVO')
        print('=' * 15)
        print()
        print('Opcoes: ')
        print('[1] VISUALIZAR AGENDA')
        print('[2] ADICIONAR UM NOVO CONTATO')
        print('[3] EDITAR UM CONTATO')
        print('[4] EXIT')

        resp = int(input('Qual opcao? '))
        if(resp == 1):
            visualizar()
        elif(resp == 2):
            addcontato()
        elif(resp == 3):
            editar()
        elif(resp == 4):
            conn.close()
            exit()

print(main())