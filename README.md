# b3irpf
Ferramenta auxiliar da declaração do imposto anual pessoa física.

# Instalação do projeto
python pip install git+https://github.com/alexsilva/b3irpf.git@master
### Instalação de dependências
python pip install -r requirements.txt
### Configuração
python manage.py makemigrations

python manage.py migrate

python manage.py setup_project
### Execução
python manage.py runserver

# Características
* Importação de dados do site do investidor (b3).
* Importação de dados por pdf (lê e registra os dados das negociações e taxas cobradas).
* Geração de relatório anual e mensal (armazenamento desses dados por posição salva manualmente).
* Relatório com lucro e prejuízos, mensais e anuais e impostos residuais (aqueles abaixo de R$ 10,00).


# Na tela adminstração (Empresas).
* registrar empresas listadas na bolsa (código, nome, cnpj, categoria).

# No site do investidor
Em https://www.investidor.b3.com.br/extrato/negociacao
* baixar o extrato em Excel com as notas de negociação do ano.

Em https://www.investidor.b3.com.br/extrato/movimentacao
* baixar o extrato em Excel com todos os provendos/outros recebidos.

# Na tela adminstração (Negociações).
* importar com o comando `importar lista de dados` os dados do arquivo Excel.


# Na tela adminstração (Proventos).
* importar com o comando `importar lista de dados` os dados do arquivo Excel.


Gerar o relatório com a compilação dos dados em Negociações (comando Relatório IRPF).
