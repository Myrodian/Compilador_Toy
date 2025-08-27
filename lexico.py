from ttoken import TOKEN

class Lexico:
    def __init__(self, arqFonte):
        self.arqFonte = arqFonte
        with open(self.arqFonte, 'r', encoding='utf-8') as f:
            self.fonte = f.read()
        self.tamFonte = len(self.fonte)
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
        print(f'(tk={msg} lex ="{lexema}" lin = {linha} col = {coluna})')

    def descartaBrancosEComentarios(self):
        while True:
            simbolo = self.getchar()
            if simbolo == '\0':
                return
            if simbolo.isspace():
                continue
            if simbolo == '//':
                while simbolo != '\n' and simbolo != '\0':
                    simbolo = self.getchar()
                continue
            self.ungetchar(simbolo)
            return

    def getToken(self):
        estado = 1
        simbolo = self.getchar()
        lexema = ''

        self.descartaBrancosEComentarios() # descarta espaços em branco e comentários
        
        lin = self.linha
        col = self.coluna

        while(True):
            if estado == 1:
                if simbolo.isalpha():
                    estado = 2 #idents, pal.reservadas
                
                elif simbolo.isdigit():
                    estado = 3 #numeros
                
                elif simbolo == '+':
                    return (TOKEN.soma, simbolo, lin, col)

                elif simbolo == '\0':
                    return (TOKEN.eof, '', self.linha, self.coluna)

            elif estado == 2:
                if simbolo.isalnum():
                    estado = 2
                else:
                    self.ungetchar(simbolo)
                    token = TOKEN.reservada(lexema)
                    return (token, lexema, lin, col)
            
            elif estado == 3:
                if simbolo.isdigit():
                    estado = 3
                else:
                    self.ungetchar(simbolo)
                    return (token, lexema, lin, col)
            elif estado == 4:

            
            if simbolo not in ['\n', '\r']:
                lexema += simbolo  # evita adicionar quebra de linha
            simbolo = self.getchar()

if __name__ == '__main__':
    lexico = Lexico("Toy-sample.txt")
    token = lexico.getToken()
    while(token[0] != TOKEN.eof):
        lexico.imprimeToken(token)
        token = lexico.getToken()
    lexico.imprimeToken(token)
