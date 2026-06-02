# 🛒 Calculadora de Preço Mínimo para Revendedores

Aplicação de terminal em Python que calcula o preço mínimo de venda de um produto com base na taxa de cada plataforma de e-commerce.

---

## 💡 Sobre o projeto

A ideia surgiu de uma necessidade real: cada plataforma cobra uma taxa diferente, e precificar errado pode fazer você trabalhar no prejuízo sem nem perceber.

A calculadora resolve isso de forma simples e direta, sem complicação.

---

## 🛍️ Plataformas suportadas

| Plataforma | Taxa aplicada |
|------------|---------------|
| Mercado Livre | 14% |
| Shopee | 20% + R$4,00 |
| Amazon Brasil | 15% |
| AliExpress | 8% |
| Tiktok Shop | 8% |

---

## ▶️ Como usar

1. Execute o arquivo `main.py`
2. Informe o nome do produto
3. Informe o valor de custo
4. Escolha a plataforma onde vai anunciar
5. Receba o preço mínimo sugerido
6. Repita para outro produto ou encerre

---

## 🖥️ Exemplo de uso

```
Bem vindo a calculadora de revenda!

Digite o nome do produto: Fone de ouvido
Digite o valor do produto: 50.00

As plataformas disponíveis são:
1. Mercado Livre
2. Shopee
3. Amazon Brasil
4. Aliexpress
5. Tiktok Shop

Qual a sua escolha: 1

No Mercado Livre, a sugestão é que o seu produto Fone de ouvido
seja vendido por, no mínimo, R$58.14

Deseja testar outro produto?
Digite Y ou N: N
```

---

## 🛠️ Tecnologias

- Python 3.10+
- `match/case` para seleção de plataforma
- `try/except` para validação de input
- `while` para repetição e controle de fluxo

---

## 🚧 Próximos passos

- Refatoração com Programação Orientada a Objetos (POO)
- Suporte a mais plataformas
- Interface gráfica ou versão web

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e contribuir.
