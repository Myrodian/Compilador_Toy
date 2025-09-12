# 🧰 Compilador Toy

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Status](https://img.shields.io/badge/status-desenvolvimento-yellow)

Repositório para o **Compilador Toy**, desenvolvido na disciplina *Compiladores I* (Curso de Ciência da Computação). Projeto didático para implementar scanner e parser (LL(1)).

---

## 📋 Sumário
- [O que é](#o-que-é)  
- [Estrutura do repositório](#estrutura-do-repositório)  
- [Como rodar](#como-rodar)  
- [Exemplo de entrada](#exemplo-de-entrada)  
- [Fluxo do compilador](#fluxo-do-compilador)  
- [Próximos passos](#próximos-passos)

---

## ❓ O que é
Mini-compilador que faz:
- 🔤 Análise léxica (`lexico.py`)
- 🌳 Análise sintática LL(1) (`sintatico.py`)
- 🧠 (futuro) análise semântica / geração de código

---

## 🗂 Estrutura do repositório
Compilador_Toy/
- ├── lexico.py # analisador léxico
- ├── sintatico.py # parser LL(1)
- ├── ttoken.py # enumeração de tokens
- ├── Toy-sample.txt # programa exemplo
- └── README.md


## ✅ Saída esperada

- ✅ **Traduzido com sucesso!**
- ❌ **Em caso de erro:** mensagem indicando a **linha** e **coluna** do problema
