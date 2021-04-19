"""
- Nome: Kristofer R.K
Trabalho 4:
- Encapsulmento
- Com menu
"""


class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        return f'Nome: {self.nome}'

    def __imprimeTelefone(self):
        return f'Telefone: {self.__telefone}'


class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimeCPF(self):
        return f'CPF: {self.__cpf}'

    def __calculaIMC(self):
        return f'IMC de altura {self.altura} e peso {self.peso} é: {self.peso / (self.altura * self.altura)}'


class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        return f'CNPJ: {self.__cnpj}'

    def __emitirNotaFiscal(self):
        return 'Nota fiscal emitida'


"""
# Testes

# Pessoa:
pessoa = Pessoa(47785, 'Kristofer', 'Rua andradas 785', '5198556845')
print(pessoa.imprimeNome())
print(pessoa._Pessoa__imprimeTelefone())

# Fisica:
fisica = Fisica(47785, 'Kristofer', 'Rua andradas 785', '5198556845', '848949646', 19, 65.0, 1.82)
print(fisica.imprimeCPF())
print(fisica._Fisica__calculaIMC())

# Juridica:
juridica = Juridica(47785, 'Kristofer', 'Rua andradas 785', '5198556845', '948118836', '42325654', 6)
print(juridica.imprimeCNPJ())
print(juridica._Juridica__emitirNotaFiscal())
"""


# Programa rodando as classes e seus métodos.


def menu():
    r = None
    while r != 7:
        print(f'==============================================================================\n'
              f'Escolha a opção\n'
              f'1) Digite 1 para cadastrar Pessoa\n'
              f'2) Digite 2 para cadastrar Pessoa Fisica\n'
              f'3) Digite 3 para cadastrar Pessoa Juridica\n'
              f'4) Digite 4 para imprimir Nome e Telefone de Pessoa\n'
              f'5) Digite 5 para imprimir o CPF e o IMC da Pessoa Fisica\n'
              f'6) Digite 6 para imprimir CNPJ e Emitir Nota Fiscal de Pessoa Juridica\n'
              f'7) Digite 7 para SAIR do programa')
        try:
            r = int(input('RESPOSTA: '))
        except ValueError:
            print('O número digitado tem que ser um inteiro')
        if r == 1:
            while True:
                try:
                    c = int(input('Digite o código: '))
                except ValueError:
                    print('O valor tem que ser um número inteiro')
                else:
                    break
            n = input('Digite o Nome: ').title()
            e = input('Digite o Endereço: ').title()
            t = input('Digite o Telefone: ')
            pessoa = Pessoa(c, n, e, t)
        elif r == 2:
            cf = input('Digite o CPF: ')
            while True:
                try:
                    i = int(input('Digite a Idade: '))
                except ValueError:
                    print('O valor tem que ser um número inteiro')
                else:
                    break
            while True:
                try:
                    pe = float(input('Digite o Peso: '))
                except ValueError:
                    print('O valor tem que ser um número')
                else:
                    break
            while True:
                try:
                    al = float(input('Digite a Altura: '))
                except ValueError:
                    print('O valor tem que ser um número')
                else:
                    break
            try:
                fisica = Fisica(c, n, e, t, cf, i, pe, al)
            except UnboundLocalError:
                print('Você precisa primeiro cadastrar uma Pessoa.')
        elif r == 3:
            cn = input('Digite o CNPJ: ')
            ie = input('Digite a Inscrição da Empresa: ')
            while True:
                try:
                    al = int(input('Digite a Quantidade de Funcionários: '))
                except ValueError:
                    print('O valor tem que ser um número inteiro')
                else:
                    break
            try:
                juridica = Juridica(c, n, e, t, cn, ie, al)
            except UnboundLocalError:
                print('Você precisa primeiro cadastrar uma Pessoa.')
        elif r == 4:
            try:
                print(pessoa.imprimeNome())
                print(pessoa._Pessoa__imprimeTelefone())
            except UnboundLocalError:
                print('Ainda não há cadastros.')
        elif r == 5:
            try:
                print(fisica.imprimeCPF())
                print(fisica._Fisica__calculaIMC())
            except UnboundLocalError:
                print('Ainda não há cadastros.')
        elif r == 6:
            try:
                print(juridica.imprimeCNPJ())
                print(juridica._Juridica__emitirNotaFiscal())
            except UnboundLocalError:
                print('Ainda não há cadastros.')
    return print('Programa finalizado com sucesso!')


menu()

