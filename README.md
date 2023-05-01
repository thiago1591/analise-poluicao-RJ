# Analise de Mobilidade Urbana RJ

### Environment

1. Create a virtualenv:
~~~bash
virtualenv --python=python3.10 venv
or
python -m venv venv	
~~~
2. Install requirements:
~~~bash
source venv/bin/activate	
~~~
~~~py
pip install -r requirements.txt
~~~

3. Run
~~~py
python app.py
~~~

### Project Organization
------------

    ├── README.md
    ├── dataset            <- Dados das DSTs
    │
    ├── notebooks          <- Notebooks para apresentação
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos e figuras
    │
    ├── requirements.txt   <- Arquivo requirements com as dependências do projeto
    │
    ├── src                <- Source code do projeto
    │   ├── __init__.py    <- Faz src ser um módulo do Python
    │   │
    │   ├── features       <- Funções que transformam os dados em features
    │   │
    │   └── visualization  <- Funções que geram a visualização dos dados
    │
    └── tox.ini            <- tox file, ver tox.readthedocs.io


--------


