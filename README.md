# API para ConsultaCA

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-092E20?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)

## Descrição

Esta é uma API para consulta de CA. Ela acessa o site [ConsultaCA](https://consultaca.com/), consulta o produto pelo Código da CA e retorna informações como as abaixo:

```json
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

Esta API foi desenvolvida para auxiliar no sistema de EPI, o [GuardEPI](https://github.com/REM-Infotech/GuardEPI), informando a validade do CA e outras informações relevantes.

## Requisitos para rodar o projeto

### Setup de ambiente:

- [PPA DeadSnakes | Apenas Linux](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)

  > Verifique a sua distribuição para o comando correto da instalação do PPA e do Python 3.11.

  ### No Ubuntu e Debian:

  - `sudo add-apt-repository ppa:deadsnakes/ppa`
  - `sudo apt update`
  - `sudo apt install python3.11`

- [Dependências do Projeto](./requirements.txt), listadas no `requirements.txt`.

## Como rodar na minha máquina?

### Instalação do `venv (Virtual Environment)`

- `python3.11 -m venv .venv`
  ou
- `python3.11 -m venv .{nomepersonalizado}`
  > Caso opte por usar um nome personalizado, adicione-o no `.gitignore` para que a pasta não seja enviada para o repositório.

### No Windows:

> É necessário habilitar a execução de scripts `.ps1` da [Microsoft](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4).

- `.venv/Scripts/activate`
- `python -m pip install -r requirements.txt`

### No Linux:

- `.venv/bin/activate`
- `python -m pip install -r requirements.txt`

### Arquivo `.env`

> Crie um arquivo `.env` com os seguintes parâmetros. Remova os comentários para evitar erros.

```python
# .env

# Parâmetro necessário para executar o sistema no modo Debug
DEBUG = True

# Configurações do banco de dados MySQL
login = ""
password = ""
host = ""
database = ""

# Token Cloudflared. Útil apenas em sistemas Linux para configuração automática do tunnel Cloudflare.
# Útil para casos de Deploy em Production
CLOUDFLARED_TOKEN = "SEU_TOKEN_AQUI"
```

## Estrutura do projeto

- [APP](./app/): Pasta centralizada com rotas, formulários e models do Flask.
- [Arquivo de Configuração](./app/default_config.py): Arquivo de configuração do APP.

### A partir de `/app`, temos:

- [Models](./app/models/): Models e binds do SQL.
- [Routes](./app/routes/): Rotas do projeto, separadas por funções.
