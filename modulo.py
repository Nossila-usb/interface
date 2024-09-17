# impota biblioteca para criacao das classes
from abc import ABC, abstractmethod

# classe abstrata, que ira funconar como uma interface
class Conta(ABC):
    # interface do possui metodos
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def fazer_deposito(self, valor):
        pass
    
    @abstractmethod
    def fazer_saque(self, valor):
        pass

# subclasse conta corrente
class ContaCorrente(Conta):
    # atributos
    def __init__(self, nome, cpf, agencia, conta, saldo): 
        self.__nome = nome
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    # GET nome
    @property
    def nome(self):
        return self.__nome
    
    # SET nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # GET cpf
    @property
    def cpf(self):
        return self.__cpf
     
    # SET cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    # GET agencia
    @property
    def agencia(self):
        return self.__agencia
    
    # SET agencia 
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    # GET conta
    @property
    def conta(self):
        return self.__conta
    
    # SET conta
    @conta.setter
    def agencia(self, conta):
        self.__conta = conta
    
    # GET saldo
    @property
    def saldo(self):
        return self.__saldo
    
    # SET saldo
    @saldo.setter
    def agencia(self, saldo):
        self.__saldo = saldo

# metodos da classe abstrata
    def consultar_saldo(self):
       return self.__saldo

    def fazer_deposito(self, valor):
      self.__saldo += valor
      return self.__saldo

    def fazer_saque(self, valor):
      self.__saldo -= valor
      return self.__saldo
