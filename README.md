# Trabalho final de BAN-1

Breve descrição do seu projeto.

## Índice

- [Instalação](#instalação)
- [Como Usar](#como-usar)

## Instalação
É necessário a instalação prévia do python em versão igual ou superior à 3.11.

Caso estaja no windows a instlação das dependências deve ser feita com o comando:

```
pip install -r requirements.txt
```


Caso estaja no Linux a instlação das dependências deve ser feita com o comando:

```
pip install -r requirements.txt 

```

Ou através do poetry, para mais segurança em um ambiente virtual
caso opte pela instalção utilizando poetry é necessário possuir 
o mesmo em seu computador, segue o comando para instalção

```
pip install poetry
```

Então dentro de seu/caminho/Ban_project/src, execute o comando:

```
poetry shell
```

logo após:

```
poetry install
```
Para fazer a intalação das dependências dentro do ambiente virtual. 

## como-usar

Dentro de seu/caminho/Ban_project/src vá ate o o arquivo Conection.py
onde vai ser feita a configuração da conexão com o banco:

```python
def get_conn():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='postgres',
        user='postgres',
        password='postgres'
    )
    return conn
```





