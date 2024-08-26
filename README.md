# API P/ Site ConsultaCA

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-092E20?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)

## Descrição

Isto é uma API de consulta de CA. Basicamente ele entra no site [`ConsultaCA`](https://consultaca.com/),
consulta o produto pelo Código da CA e trás informações como essas abaixo:

``` json

{
    "aprovado_para": "PROTEÇÃO DO CRÂNIO E FACE DO USUÁRIO CONTRA RISCOS PROVENIENTES DE FONTES GERADORAS DE CALOR NOS TRABALHOS DE COMBATE A INCÊNDIO.",
    "ca": "VÁLIDO",
    "cnpj_do_laboratório": "10.000.000/0000-10",
    "cnpj_importador": "45.655.461/0001-30",
    "cod_ca": "13037",
    "cor": "Diversas.",
    "deixe_suaavaliação": "",
    "feito_com_por_safetytec_tecnologia_e_inovação_em_seg._do_trabalho_ltda._-_cnpj": "14.957.619/0001-01",
    "laudo": "SEI nº FF MSA 17",
    "marcar_comofavorito": "",
    "marcação": "Parte interna do casco.",
    "natureza": "Importado",
    "processo": "19980212903202378",
    "razão_social": "SAFETY EQUIPMENT INSTITUTE",
    "razão_social_importador": "MSA DO BRASIL EQUIP E INSTRUMENTOS DE SEGURANCA LTDA",
    "referências": "CAPACETE PARA BOMBEIROS MSA CAIRNS 660",
    "registardúvida": "",
    "validade": "20/11/2028"
}

```

Fiz ela para me auxiliar no meu sistema de EPI, o [`GuardEPI`](https://github.com/REM-Infotech/GuardEPI), para informar
a validade do CA e afins


## Requisitos para rodar o projeto

### Setup de ambiente:

- [`PPA DeadSnakes | Apenas Linux`](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
    > Verificar qual sua distro para o comando correto da instalação do PPA e instalação do python 3.11
    ### No ubuntu e debian (Normalmente utilizados para projetos):
    - `sudo add-apt-repository ppa:deadsnakes/ppa`
    - `sudo apt update`
    - `sudo apt install python3.11`

- [`Dependências do Projeto`](./requirements.txt), estarão em `requirements.txt`

## Como rodar na minha máquina?

#### Instalação do `venv (Virtual Environment)`

- `python3.11 -m venv .venv` 
ou
- `python3.11 -m venv .{nomepersonalizado}` 
    > Caso opte por usar um nome personalizado, adicionar o mesmo no `.gitignore` para a pasta não subir para o repositório

#### No Windows:
> Necessário habilitar execução de scripts `.ps1` da [Microsoft](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4)
- `.venv/Scripts/activate`
- `python -m pip install -r requirements.txt`

#### No Linux:

- `.venv/bin/activate`
- `python -m pip install -r requirements.txt`


#### Arquivo `.env`

> Crie um arquivo .env com esses parametros. Remova os comentários para evitar erros

``` Python

## .env

## Parâmetro necessário para executar o sistema no modo Debug
DEBUG = True

## Configurações do banco de dados MySQL
login = ""
password = ""
host = ""
database = ""

## Token Cloudflared. Ele será útil apenas em um sistema linux
## Pois ele fará a configuração automatica do tunnel Cloudflare.
## Útil para casos de Deploy em Production
CLOUDFLARED_TOKEN = "SEU_TOKEN_AQUI"


``` 


## Estrutura do projeto

- [`APP`](./app/): É a pasta onde fica centralizado rotas, formulários e models do Flask

- [`Arquivo Config.`](./app/default_config.py): Arquivo de configuração do APP

#### A partir de `/app`, teremos:
- [`Models`](./app/models/): Onde ficam os models e bind's do SQL.

- [`Routes`](./app/routes/): Formulários do projeto, sempre mantendo separados por funções.


