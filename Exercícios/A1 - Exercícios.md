### Cenário 1

Tarefa: Alterar o banco de dados para o MariaDB

#### Perguntas

- O que precisou ser alterado?
- Qual foi o impacto na aplicação?


### Cenário 2

Tarefa: Alterar a porta da aplicação de 8000 para 9000

#### Perguntas

- O que precisou ser alterado?
- Qual foi o impacto na aplicação?

### Cenário 3

Tarefa: Alterar a porta padrão do banco de dados

#### Perguntas

- O que precisou ser alterado?
- Qual foi o impacto na aplicação?


### Cenário 4

Tarefa: Delete o volume do container do banco de dados

#### Perguntas

- Qual foi o impacto na aplicação?
- O que isso impacta em ambientes de produção?


### Cenário 5

Tarefa: Parar apenas o container do banco de dados

#### Perguntas

- Qual foi o comportamento da aplicação?
- Retorne o banco de dados. Como foi o comportamento após essa ação?
- Existe retry de conexão?


### Cenário 6

Tarefa: Criar uma nova rede e mover apenas a API para ela. Após isso, testar a comunicação com o banco de dados.

#### Perguntas

- A API conseguiu acessar o banco de dados?
- Qual a importância disso no aspecto de segurança?

### Cenário 7

Atualmente o banco de dados está na mesma rede interna do Docker e não está exposto publicamente.Imagine que um desenvolvedor decide expor a porta do banco no docker compose para facilitar testes externos.


#### Perguntas

- Quais riscos essa decisão pode gerar em um ambiente real?
- Como um invasor poderia descobrir essa porta aberta?
- Como você mitigaria esse risco?
- Que tipo de ataque pode acontecer?