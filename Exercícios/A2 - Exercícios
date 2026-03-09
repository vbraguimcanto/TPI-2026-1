
# Exercícios – Function Calling em Python (via Mensagem)

Estes exercícios têm como objetivo ensinar o conceito de Function Calling em Python utilizando mensagens em linguagem natural, simulando o comportamento de agentes com ferramentas (tools).

Os exercícios começam com exemplos simples de interpretação de mensagens e evoluem até consultas em banco de dados.

---

# Exercício 1 — Calculadora Simples

Crie duas funções:

```python
def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b
```

O programa deve receber uma mensagem do usuário, por exemplo:

```
Quanto é 5 + 3?
```

ou

```
Multiplique 4 por 7
```

O sistema deve:

1. Interpretar a mensagem  
2. Identificar a operação  
3. Chamar a função correta  
4. Mostrar o resultado

---

# Exercício 2 — Calculadora Completa

Implemente as funções:

- `somar`
- `subtrair`
- `multiplicar`
- `dividir`

Exemplos de mensagens:

```
Quanto é 10 dividido por 2?
```

```
Calcule 15 menos 8
```

O sistema deve identificar automaticamente qual função chamar.

---

# Exercício 3 — Conversão de Temperatura

Crie as funções:

- `celsius_para_fahrenheit`
- `fahrenheit_para_celsius`

Mensagens possíveis:

```
Converter 30 graus Celsius para Fahrenheit
```

```
Quanto é 80F em Celsius?
```

O programa deve interpretar a mensagem e chamar a função correta.

---

# Exercício 4 — Consulta de Produto

Crie a função:

```
buscar_produto(nome_produto)
```

Use um dicionário como base de dados:

```python
produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}
```

Mensagens possíveis:

```
Qual o preço do notebook?
```

```
Quanto custa um mouse?
```

O sistema deve identificar o produto e chamar `buscar_produto`.

---

# Exercício 5 — Verificação de Estoque

Crie funções:

- `buscar_produto`
- `verificar_estoque`

Base de dados:

```python
estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}
```

Mensagens possíveis:

```
Tem notebook em estoque?
```

```
Quantos mouses temos?
```

O sistema deve decidir qual função chamar.

---

# Exercício 6 — Sistema de Agenda

Crie funções:

```
criar_evento(titulo, data)
listar_eventos()
```

Armazene eventos em uma lista.

Mensagens possíveis:

```
Criar evento reunião amanhã
```

```
Mostrar meus eventos
```

O sistema deve interpretar a mensagem e chamar a função correta.

---

# Exercício 7 — Consulta de Clima

Crie a função:

```
buscar_clima(cidade)
```

Base de dados fictícia:

```python
clima = {
    "sao paulo": "24°C e nublado",
    "bauru": "30°C e ensolarado",
    "curitiba": "18°C e chuvoso"
}
```

Mensagens possíveis:

```
Como está o clima em Bauru?
```

```
Qual a temperatura em Curitiba?
```

O programa deve extrair o nome da cidade e chamar a função.

---

# Exercício 8 — Consulta em Banco de Dados (Produtos)

Crie um banco **SQLite** chamado:

```
loja.db
```

Tabela:

```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL
);
```

Insira alguns dados:

```
notebook – 4500
mouse – 80
teclado – 150
monitor – 900
```

Crie a função:

```
buscar_produto(nome_produto)
```

Ela deve:

1. Conectar no banco
2. Buscar o produto
3. Retornar o preço

Mensagem exemplo:

```
Qual o preço do notebook?
```

---

# Exercício 9 — Consulta de Clientes no Banco

Crie uma tabela:

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cidade TEXT
);
```

Dados de exemplo:

```
Ana – Bauru
Carlos – São Paulo
Mariana – Curitiba
Pedro – Bauru
```

Crie a função:

```
buscar_clientes_por_cidade(cidade)
```

Mensagens possíveis:

```
Quais clientes são de Bauru?
```

```
Mostre clientes de São Paulo
```

O sistema deve:

1. Interpretar a cidade
2. Executar a consulta no banco
3. Mostrar os clientes encontrados

---

# Exercício 10 — Agente que Consulta Pedidos

Crie tabela:

```sql
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente TEXT,
    produto TEXT,
    valor REAL
);
```

Exemplo de dados:

```
1 | Ana | Notebook | 4500
2 | Carlos | Mouse | 80
3 | Ana | Teclado | 150
```

Crie funções:

```
buscar_pedidos_cliente(nome)
valor_total_cliente(nome)
```

Mensagens possíveis:

```
Quais pedidos a Ana fez?
```

```
Qual o valor total das compras da Ana?
```

O sistema deve:

1. Interpretar a mensagem
2. Escolher a função correta
3. Consultar o banco
4. Mostrar o resultado

