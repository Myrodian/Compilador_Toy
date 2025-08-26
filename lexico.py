from ttoken import TOKEN

class Lexico:
    def __init__(self, arqFonte):
        self.arqFonte = arqFonte
        self.Fonte = self.arqFonte.read()
        self.tamFonte = len(self.Fonte)
        self.indiceFonte = 0
        self.tokenLido = None
        self.linha = 1
        self.coluna = 0

    def fimDoArquivo(self):
        return self.indiceFonte >= self.tamFonte
    
    def getchar(self):
        if self.fimDoArquivo():
            return '\0'
        car = self.fonte[self.indiceFonte]
        self.indiceFonte += 1
        if car == '\n':
            self.linha += 1
            self.coluna = 0
        else:
            self.coluna += 1
        return car

    def ungetchar(self, simbolo):
        if simbolo == '\n':
            self.linha -= 1
        if self.indiceFonte > 0:
            self.indiceFonte -=1
        self.coluna -= 1

    def imprimeToken(self, tokenCorrente):
        (token, lexema, linha, coluna) = tokenCorrente
        msg = TOKEN.msg(token)
        print(f'(tk={msg}lex = "{lexema}"lin = {linha} col = {coluna})')

    def getToken(self):
        estado = 1
        simbolo = self.getchar()
        lexema = ''

        self.descartaBrancosEComentarios() #fazer essa função para descartar comentarios
        
        lin = self.linha
        col = self.coluna
        while(True):
            if estado == 1:
                if simbolo.isalpha():
                    estado = 2 #idents, pal.reservadas
                elif simbolo.isdigit():
                    estado = 3 #numeros
            elif estado == 2:
                if simbolo.isalnum():
                    estado = 2
                else:
                    self.ungetchar(simbolo)
                    token = TOKEN.reservada(lexema)
                    return (token, lexema, lin, col)

            lexema = lexema + simbolo
            simbolo = self.getchar()

if __name__ == '__main__':
    lexico = Lexico("teste.toy")
    token = lexico.getToken()
    while(token[0] != TOKEN.eof):
        lexico.imprimeToken(token)
        token = lexico.getToken()
    lexico.imprimeToken(token)
