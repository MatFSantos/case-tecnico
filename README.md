# Organizador de Tabelas e Dashboard interativo

Esse repositório é destinado ao script organizador de tabelas de dados e também ao Dashboard interativo capaz de analisar dados de diversas formas e de diversas visões diferentes com gráficos variados.

## Como usar

Nesta sessão você saberá como executar ambos os recursos desse repositório localmente em seu computador.

- Primeiramente tenha o python instalado em sua máquina, de preferência a versão que consta no arquivo `.python-version`.
- Após isso garantido, instale as dependências do código presentes em `requirements.txt`. Você pode fazer isso executando o seguinte comando na pasta do arquivo mencionado:
    ```
    $ pip install -r requirements.txt
    ```
- Após isso você já está apto a executar os arquivos de organização de tabelas e do dashboard interativo.

### Organizador de tabelas

Esse script organiza tabelas que possuem uma característica ímpar: tabelas `.xlsx` ou `.csv` de coluna única, ou seja, todas as colunas da tabela devem estar em uma única coluna, separados por `;`.

Existem três arquivos principais para o **Organizador**: `filer.py`,`organizer.py` e `run.py`.

- `filer.py`: Esse arquivo é responsável por abrir os arquivos de tabelas com os dados, e conta com uma classe que faz todo o trabalho;
- `organizer.py`: Esse arquivo faz a organização total da tabela e a divide em três tabelas diferentes: dados comuns, dados de fornecedor e dados de destinatário;
- `run.py`: nesse arquivo é feito a integração dos outros dois e o salvamento dos novos arquivos, se assim for desejado.

Para executar o **Organizador**, você deve executar o seguinte comando:
```
$ python run.py
```
Isso iniciará o módulo e fará todo o processo, siga as instruções e processo será concluido com sucesso.

Ainda para a execução, você pode usar duas flags importantes: `--save` e `--file`. A primeira indica se o resultado do processamento dos dados deve ser salvo ou não, já a segunda indica os arquivos que serão utilizados para o processamento, sendo o primeiro os dados crus e o segundo o arquivo complementar, com as descrições de cancelamento. Um exemplo a seguir de como utilizar:

```
$ python run.py --save --file ./spreadsheets/dados.xlsx ./spreadsheet/codigo_cancelamento.xlsx
```

> OBS: caso não seja passada a flag `--file`, o script perguntará para o usuário qual arquivo ele deseja utilizar dos arquivos que estão dentro da pasta `spreadsheets/`.

> OBS: caso não seja passada a flag `--save`, o script não salvará o resultado e somente fará o processo de organização das planilhas e imprimirá o resultado no promp.

### Dashborad interativo

O Dashboard usa uma biblioteca Python para fazer todo o processo, a [Streamlit](https://streamlit.io/). Então para executar o dashboard localmente, basta usar o comando:
```
$ streamlit run dashboard.py
```

Isso executará todo o código do arquivo `dashboard.py`. O servidor local será aberto e você poderá acessar pelo navegador.

> OBS: Lembre de conferir o código, pois ele está abrindo planilhas com nomes específicos. Mude se necessário.