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
        print(f'(token = {msg}\t lex = "{lexema}" \t lin = {linha} col = {coluna})')

    def getToken(self):
        estado = 1
        simbolo = self.getchar()
        lexema = ''
        
        lin = self.linha
        col = self.coluna

        while(True):
            if estado == 1:
                if simbolo.isalpha():
                    estado = 2 #idents, pal.reservadas
                
                elif simbolo.isdigit():
                    estado = 3 #numeros
                
                elif simbolo == '/':  # pode ser divisão ou comentário
                    estado = 4
                
                elif simbolo == '=': # verificar se é comparação ou atribuição
                    estado = 5

                elif simbolo == '<':
                    estado = 6

                elif simbolo == '>':
                    estado = 7

                elif simbolo == '\'':
                    estado = 8
                
                elif simbolo == '\"':
                    estado = 9

                elif simbolo == '!':
                    estado = 10
                elif simbolo == '+':
                    return (TOKEN.mais, simbolo, lin, col)
                
                elif simbolo == '-':
                    return (TOKEN.menos, simbolo, lin, col)
                
                elif simbolo == '*':
                    return (TOKEN.multiplica, simbolo, lin, col)
                
                elif simbolo == '(':
                    return(TOKEN.abrePar, simbolo, lin, col)
                
                elif simbolo == ')':
                    return(TOKEN.fechaPar, simbolo, lin, col)
                
                elif simbolo == '{':
                    return(TOKEN.abreChave, simbolo, lin, col)
                
                elif simbolo == '}':
                    return(TOKEN.fechaChave, simbolo, lin, col)
                
                elif simbolo == ',':
                    return (TOKEN.virg, simbolo, lin, col)

                elif simbolo == ';':
                    return (TOKEN.ptoVirg, simbolo, lin, col)
                
                elif simbolo == '.':
                    return (TOKEN.pto, simbolo, lin, col)

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
                if simbolo.isdigit() or simbolo == ".":
                    estado = 3
                elif simbolo.isalpha():
                    return (TOKEN.erro, lexema, lin, col)
                else:
                    self.ungetchar(simbolo)
                    return (TOKEN.num, lexema, lin, col)
                
            elif estado == 4:
                if simbolo == '/':  # é comentário
                    # descarta até fim da linha
                    while simbolo != '\n' and simbolo != '\0':
                        simbolo = self.getchar()
                    return self.getToken()  # continua analisando depois do comentário
                else:
                    self.ungetchar(simbolo)  # não era comentário, devolve o caractere
                    return (TOKEN.divide, lexema, lin, col)
                
            elif estado == 5:
                if simbolo == '=':
                    return (TOKEN.igual, lexema, lin, col)
                else:
                    self.ungetchar(simbolo) # não era igualdade, devolve o caractere
                    return (TOKEN.atrib, lexema, lin, col)
            
            elif estado == 6:
                if simbolo == '=':
                    return (TOKEN.menorIgual, lexema, lin, col)
                else:
                    self.ungetchar(simbolo) # não era menorIgual, devolve o caractere
                    return (TOKEN.menor, lexema, lin, col)
            elif estado == 7:
                if simbolo == '=':
                    return (TOKEN.maiorIgual, lexema, lin, col)
                else:
                    self.ungetchar(simbolo) # não era maiorIgual, devolve o caractere
                    return (TOKEN.maior, lexema, lin, col)
            elif estado == 8:
                if simbolo == '\'':
                    return (TOKEN.string, lexema, lin, col)
                
            elif estado == 9:
                if simbolo == '\"':
                    return (TOKEN.string, lexema, lin, col)
            elif estado == 10:
                if simbolo == '=':
                    return (TOKEN.diferente, lexema, lin, col)
                else:
                    self.ungetchar(simbolo)
                    return (TOKEN.erro, lexema, lin, col)
                
            if simbolo not in ['\n', '\r']:
                if estado == 8 or estado == 9: # quando for string ele mantém os espaços em branco no lexema
                    lexema += simbolo
                else:
                    if simbolo not in [' ', '\t']: #quando não é string ele retira os espaços em branco do lexema
                        lexema += simbolo  # evita adicionar quebra de linha
            simbolo = self.getchar()

if __name__ == '__main__':
    lexico = Lexico("Toy-sample.txt")
    token = lexico.getToken()
    while(token[0] != TOKEN.eof):
        lexico.imprimeToken(token)
        token = lexico.getToken()
    lexico.imprimeToken(token)
