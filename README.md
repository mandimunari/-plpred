```
# plpred

By Amanda Munari Guimaraes

a protein subcellular location prediction program

## Setup

```
$ make setup
```
## Estrutura do Projeto

### - `environment.yml`
É um tipo que arquivo que tem como finalidade de definir quais são as aplicações e requisitos necessários para a implementação de um projeto.

### - `requirements.txt`
O arquivo *requirements.txt*  contém uma lista de itens ou pacotes que serão instalados durante o *pip install*.

### - `Makefile`
No Makefile temos as especificações das regras que podem ser executadas. Basicamente o makefile é um arquivo para configuração de compilação utilizado pelo programa Make, cuja idéia é simplificar e agilizar a compilação de programas. 

### - Data
No diretório data encontram-se os diretórios raw e processed. No diretório raw é onde se encontram os arquivos de banco de dados original. No diretório processed é onde se encontra o arquivo com os dados pré processados.

### - plpred
No diretório plpred é onde todos os script em python estão armazenados.

### - `plpred-server`

usage: plpred-server [-h] -H HOST -p PORT -m MODEL

plpred-server: subcellular location prediction server

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  host address
  -p PORT, --port PORT  host port
  -m MODEL, --model MODEL
```