#---------------------------------------------------
# Tradutor para a linguagem CALC
#
# versao 1a (mar-2024)
#---------------------------------------------------

from enum import IntEnum
class TOKEN(IntEnum):
    erro = 1
    eof = 2
    ident = 3
    num = 4
    string = 5
    IF = 6
    ELSE = 7
    INICIO = 8
    FIM = 9
    PROG = 10
    abrePar = 11
    fechaPar = 12
    virg = 13
    ptoVirg = 14
    pto = 15
    igual = 16
    diferente = 17
    menor = 18
    menorIgual = 19
    maior = 20
    maiorIgual = 21
    AND = 22
    OR = 23
    NOT = 24
    mais = 25
    menos = 26
    multiplica = 27
    divide = 28
    LEIA = 29
    ESCREVA = 30
    abreChave = 31
    fechaChave = 32
    atrib = 33

    @classmethod
    def msg(cls, token):
        nomes = {
            1:'erro',
            2:'<eof>',
            3:'ident',
            4:'numero',
            5:'string',
            6:'if',
            7:'else',
            8:'inicio',
            9:'fim',
            10:'prog',
            11:'(',
            12:')',
            13:',',
            14:';',
            15:'.',
            16:'=',
            17:'==',
            18:'!=',
            19:'<',
            20:'<=',
            21:'>',
            22:'>=',
            23:'and',
            24:'or',
            25:'not',
            26:'+',
            27:'-',
            28:'*',
            29:'/',
            30:'leia',
            31:'escreva',
            33:'{',
            34:'}',
        }
        return nomes[token]

    @classmethod
    def reservada(cls, lexema):
        reservadas = {
            'program': TOKEN.PROG,
            'if': TOKEN.IF,
            'begin': TOKEN.INICIO,
            'end': TOKEN.FIM,
            'else': TOKEN.ELSE,
            'leia': TOKEN.LEIA,
            'escreva': TOKEN.ESCREVA,
            'and': TOKEN.AND,
            'or': TOKEN.OR,
            'not': TOKEN.NOT
        }
        if lexema in reservadas:
            return reservadas[lexema]
        else:
            return TOKEN.ident
