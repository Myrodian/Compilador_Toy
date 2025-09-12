from ttoken import TOKEN
from lexico import Lexico

class Sintatico:
    def __init__(self, nomeArquivo):
        self.lexico = Lexico(nomeArquivo)
        self.tokenLido = None

    def traduz(self):
        self.tokenLido = self.lexico.getToken()
        try:
            self.prog()
            self.consome(TOKEN.eof)
            print("Traduzido com sucesso!")
        except Exception as e:
            print("Erro sintático:", e)

    def consome(self, tokenEsperado):
        (token, lexema, linha, coluna) = self.tokenLido
        if token == tokenEsperado:
            self.tokenLido = self.lexico.getToken()
        else:
            msgTokenLido = TOKEN.msg(token)
            msgTokenEsperado = TOKEN.msg(tokenEsperado)
            raise Exception(f"Linha {linha}, coluna {coluna}: esperado {msgTokenEsperado}, encontrado {msgTokenLido}")

    # ------------------ Regras da Gramática ------------------

    def prog(self):
        self.consome(TOKEN.INICIO)
        self.coms()
        self.consome(TOKEN.FIM)
        self.consome(TOKEN.pto)

    def coms(self):
        if self.tokenLido[0] in (TOKEN.FIM, TOKEN.fechaChave):
            return  # LAMBDA
        self.com()
        self.coms()

    def com(self):
        if self.tokenLido[0] == TOKEN.LEIA:
            self.ler()
        elif self.tokenLido[0] == TOKEN.ESCREVA:
            self.escrever()
        elif self.tokenLido[0] == TOKEN.IF:
            self.if_()
        elif self.tokenLido[0] == TOKEN.ident:
            self.atrib()
        elif self.tokenLido[0] == TOKEN.abreChave:
            self.bloco()
        else:
            self.erro("Comando inválido")

    def ler(self):
        self.consome(TOKEN.LEIA)
        self.consome(TOKEN.abrePar)
        self.consome(TOKEN.string)
        self.consome(TOKEN.virg)
        self.consome(TOKEN.ident)
        self.consome(TOKEN.fechaPar)
        self.consome(TOKEN.ptoVirg)

    def escrever(self):
        self.consome(TOKEN.ESCREVA)
        self.consome(TOKEN.abrePar)
        self.consome(TOKEN.string)
        self.restoEscrever()

    def restoEscrever(self):
        if self.tokenLido[0] == TOKEN.virg:
            self.consome(TOKEN.virg)
            self.consome(TOKEN.ident)
            self.consome(TOKEN.fechaPar)
            self.consome(TOKEN.ptoVirg)
        elif self.tokenLido[0] == TOKEN.fechaPar:
            self.consome(TOKEN.fechaPar)
            self.consome(TOKEN.ptoVirg)
        else:
            self.erro("Erro em escreva")

    def if_(self):
        self.consome(TOKEN.IF)
        self.consome(TOKEN.abrePar)
        self.exp()
        self.consome(TOKEN.fechaPar)
        self.com()
        self.restoIf()

    def restoIf(self):
        if self.tokenLido[0] == TOKEN.ELSE:
            self.consome(TOKEN.ELSE)
            self.com()

    def bloco(self):
        self.consome(TOKEN.abreChave)
        self.coms()
        self.consome(TOKEN.fechaChave)

    def atrib(self):
        self.consome(TOKEN.ident)
        self.consome(TOKEN.atrib)
        self.exp()
        self.consome(TOKEN.ptoVirg)

    # ------------------ Expressões ------------------

    def exp(self):
        self.nao()
        self.restoExp()

    def restoExp(self):
        if self.tokenLido[0] == TOKEN.AND:
            self.consome(TOKEN.AND)
            self.nao()
            self.restoExp()
        elif self.tokenLido[0] == TOKEN.OR:
            self.consome(TOKEN.OR)
            self.nao()
            self.restoExp()

    def nao(self):
        if self.tokenLido[0] == TOKEN.NOT:
            self.consome(TOKEN.NOT)
            self.nao()
        else:
            self.rel()

    def rel(self):
        self.soma()
        self.restoRel()

    def restoRel(self):
        if self.tokenLido[0] in (TOKEN.igual, TOKEN.diferente, TOKEN.menor, TOKEN.menorIgual, TOKEN.maior, TOKEN.maiorIgual):
            self.consome(self.tokenLido[0])
            self.soma()

    def soma(self):
        self.mult()
        self.restoSoma()

    def restoSoma(self):
        if self.tokenLido[0] == TOKEN.mais:
            self.consome(TOKEN.mais)
            self.mult()
            self.restoSoma()
        elif self.tokenLido[0] == TOKEN.menos:
            self.consome(TOKEN.menos)
            self.mult()
            self.restoSoma()

    def mult(self):
        self.uno()
        self.restoMult()

    def restoMult(self):
        if self.tokenLido[0] == TOKEN.multiplica:
            self.consome(TOKEN.multiplica)
            self.uno()
            self.restoMult()
        elif self.tokenLido[0] == TOKEN.divide:
            self.consome(TOKEN.divide)
            self.uno()
            self.restoMult()

    def uno(self):
        if self.tokenLido[0] == TOKEN.mais:
            self.consome(TOKEN.mais)
            self.uno()
        elif self.tokenLido[0] == TOKEN.menos:
            self.consome(TOKEN.menos)
            self.uno()
        else:
            self.folha()

    def folha(self):
        if self.tokenLido[0] == TOKEN.num:
            self.consome(TOKEN.num)
        elif self.tokenLido[0] == TOKEN.ident:
            self.consome(TOKEN.ident)
        elif self.tokenLido[0] == TOKEN.abrePar:
            self.consome(TOKEN.abrePar)
            self.exp()
            self.consome(TOKEN.fechaPar)
        else:
            self.erro("Fator inválido")

    def erro(self, msg):
        (token, lexema, linha, coluna) = self.tokenLido
        raise Exception(f"Linha {linha}, coluna {coluna}: {msg}, encontrado {TOKEN.msg(token)}")

if __name__ == "__main__":
    s = Sintatico("Toy-sample.txt")
    s.traduz()