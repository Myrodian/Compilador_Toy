🧰 Compilador Toy

Projeto desenvolvido para a disciplina Compiladores I do curso de Ciência da Computação 🎓.
Objetivo: implementar um mini-compilador usando análise léxica, sintática (LL(1)) e, futuramente, semântica.

📚 O que faz

🔤 Análise Léxica → converte o código-fonte em tokens

🌳 Análise Sintática (LL(1)) → valida a estrutura segundo a gramática

🧠 (Futuro) → análise semântica e geração de código

🗂 Estrutura
Compilador_Toy/
├── lexico.py      # Analisador léxico
├── sintatico.py   # Parser LL(1)
├── ttoken.py      # Definição de tokens
├── Toy-sample.txt # Programa exemplo
└── README.md

🚀 Como usar
git clone https://github.com/seu-usuario/Compilador_Toy.git
cd Compilador_Toy
python sintatico.py


✅ Saída: Traduzido com sucesso!
❌ Erro: mostra linha e coluna do problema

🧪 Exemplo
inicio
    leia("Digite um valor", x);
    escreva("Valor lido: ", x);
    if (x > 0)
        escreva("Positivo");
    else
        escreva("Não positivo");
fim.

🔄 Fluxo do Compilador
graph LR
A[Código-Fonte] --> B[🔤 Léxico]
B --> C[🌳 Sintático (LL1)]
C --> D[🧠 Semântico (futuro)]
D --> E[⚙️ Código Intermediário]

🎯 Objetivos

Entender autômatos e gramáticas LL(1)

Construir um parser de descida recursiva

Evoluir para análise semântica e geração de código
