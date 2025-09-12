🧰 Compilador Toy

Compilador_Toy é um projeto desenvolvido para a disciplina Compiladores I do curso de Ciência da Computação.
O objetivo é implementar um compilador simples (Toy) para uma linguagem fictícia, aplicando os conceitos de análise léxica, sintática e semântica aprendidos em aula.

📚 Descrição do Projeto

Este compilador é dividido em três fases principais:

🔤 Analisador Léxico

Implementado em lexico.py

Lê o código-fonte caractere por caractere

Constrói tokens usando um autômato de estados finitos

Identifica palavras reservadas, identificadores, números, operadores e símbolos

🌳 Analisador Sintático (Parser)

Implementado em sintatico.py

Baseado em parsing LL(1) e descida recursiva

Verifica se a sequência de tokens está de acordo com a gramática:

Prog -> inicio Coms fim .
Coms -> LAMBDA | Com Coms
Com  -> Ler | Escrever | If | Atrib | Bloco
Ler  -> leia ( string, ident ) ;
Escrever -> escreva ( string RestoEscrever
RestoEscrever -> , ident ) ; | ) ;
If -> if ( Exp ) Com RestoIf
RestoIf -> LAMBDA | else Com
Bloco -> { Coms }
Atrib -> ident = Exp ;
...


🧠 (Fase futura) Analisador Semântico / Geração de Código

Em desenvolvimento

Responsável por verificar tipos, escopos e gerar código intermediário ou final

🗂 Estrutura do Repositório
Compilador_Toy/
│
├── lexico.py        # 🔤 Implementação do analisador léxico
├── sintatico.py     # 🌳 Implementação do analisador sintático (LL(1))
├── ttoken.py        # 🏷️ Enumeração de tokens e mensagens
├── Toy-sample.txt   # 📄 Programa exemplo para testes
└── README.md        # 📘 Este arquivo

🚀 Como Executar

Pré-requisito: Python 3.10+ instalado

Clone o repositório

git clone https://github.com/seu-usuario/Compilador_Toy.git
cd Compilador_Toy


Execute o compilador

python sintatico.py


Veja a saída

Se o programa estiver correto → ✅ “Traduzido com sucesso!”

Caso contrário → ❌ Erro sintático com linha e coluna

🧪 Exemplo de Programa de Entrada
inicio
    leia("Digite um valor", x);
    escreva("Valor lido: ", x);
    if (x > 0)
        escreva("Positivo");
    else
        escreva("Não positivo");
fim.

👨‍💻 Equipe

Você – Estudante de Ciência da Computação ✍️

Projeto desenvolvido como parte da disciplina Compiladores I

🎯 Objetivos Didáticos

✅ Entender como funciona um analisador léxico (scanner)

✅ Implementar um parser recursivo descendente LL(1)

⏳ Implementar análise semântica e geração de código

🎓 Consolidar os conceitos da disciplina de compiladores

🛠 Tecnologias

Linguagem: Python 3 🐍

Paradigma: Descida recursiva para parsing

Conceitos: Teoria da compilação, autômatos, gramáticas LL(1)

💡 Próximos Passos

🧠 Adicionar análise semântica (tabela de símbolos)

⚙️ Implementar geração de código intermediário

🧪 Criar mais casos de teste para validação
