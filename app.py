

import os
from modulo import *

# NOTE: programa pricipal
if __name__ == "__main__":
    cc = ContaCorrente('','', '1001-1', '10010-1', 0)

    # entrada de dados 
    cc.nome = input('Informe o nome so titular: ')
    cc.cpf = input('Informe o cpf do titular: ')

    

while True: 
     # saida de dados
     print(f'Nome: {cc.nome}.')
     print(f'CPF: {cc.cpf}.')
     print(f'Agencia: {cc.agencia}.')
     print(f'conta: {cc.conta}.')
     print(f'Saldo: : {cc.saldo}.')
     
     # NOTE: exine menu
     print('1 - comsultar saldo.')
     print('2 - fazer deposito.')
     print('3 - fazer saque.')
     print('4 - sair do pgrama.')

     # usuario informa a opção desejada
     opcao = input('Informe a opção desejada: ')

     # limpa sistema
     os.system('cls')

     match opcao:
        case '1':
           print('Consultar saldo\n')
           print(f'Saldo disponivel: R$ {cc.consultar_saldo():,.2f}.')
           continue
        case '2':
           valor = float(input('Valor do deposito: R$').replace(',','.'))
           if valor > 0:
              cc.saldo = cc.fazer_deposito(valor)
              print('Deposito efetuado com sucesso.')
           else:
              print('Valor invalido.')
           continue
        case '3':
           valor = float(input('Valor de saque: R$ ').replace(',','.'))
           if valor <= cc.saldo:
              cc.saldo = cc.fazer_saque(valor)
              print('Saque efetuado com sucesso.')
           else:
              print('Não foi possivel efetuar o saque.')
           continue
        case '4':
           print('Programa encerrado.')
           break
        case _:
           print('Opção invalida')
           continue


