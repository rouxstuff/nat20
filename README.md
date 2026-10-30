# Nat20🌿

Aplicação web para criar e gerenciar fichas de RPG, começando por **D&D 5e**. Os modificadores, bônus de proficiência, perícias e testes de resistência são calculados automaticamente a partir dos atributos do personagem.

> **Status:** em desenvolvimento. Projeto de estudo de API e desenvolvimento web com Python.

## Funcionalidades

- [x] Regras de D&D 5e: modificadores, proficiência, perícias, testes de resistência, iniciativa e percepção passiva
- [x] Configuração por variáveis de ambiente
- [x] Conexão com o banco de dados (SQLite no desenvolvimento)
- [ ] Modelos do banco: usuários, personagens e itens
- [ ] CRUD de personagens
- [ ] Ficha com valores calculados (`/characters/{id}/sheet`)
- [ ] Cadastro e login (JWT)
- [ ] Interface web da ficha
- [ ] Rolador de dados (`2d6+3`)
- [ ] Busca de magias e equipamentos na [D&D 5e API](https://www.dnd5eapi.co/)
- [ ] Link público para compartilhar a ficha
- [ ] Deploy

## Tecnologias

- [Python](https://www.python.org/) 3.11+
- [FastAPI](https://fastapi.tiangolo.com/): API e documentação interativa
- [SQLAlchemy](https://www.sqlalchemy.org/) 2.0: acesso ao banco de dados
- [Pydantic](https://docs.pydantic.dev/): validação de dados e configurações
- SQLite (desenvolvimento) e PostgreSQL (produção)

## Como rodar localmente

### Pré-requisitos

- Python 3.11 ou mais novo
- Git

### Instalação

```bash
git clone https://github.com/SEU-USUARIO/nat20.git
cd nat20

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env             # Windows: Copy-Item .env.example .env
```

Abra o arquivo `.env` e troque o valor de `SECRET_KEY`. Para gerar uma chave:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Executando

```bash
uvicorn app.main:app --reload
```

- API: http://127.0.0.1:8000
- Documentação interativa (Swagger): http://127.0.0.1:8000/docs
- Verificação de saúde: http://127.0.0.1:8000/health

## Variáveis de ambiente

| Variável | Descrição | Exemplo |
|---|---|---|
| `DATABASE_URL` | URL de conexão com o banco | `sqlite:///./nat20.db` |
| `SECRET_KEY` | Chave usada para assinar os tokens de login | gerada com `secrets.token_hex(32)` |

O arquivo `.env` **não** é versionado. Use o `.env.example` como modelo.

## Estrutura do projeto

```
nat20/
├── app/
│   ├── main.py            # criação do app e rotas
│   ├── config.py          # leitura das variáveis de ambiente
│   ├── database.py        # engine, sessão e get_db
│   ├── models.py          # tabelas (User, Character, Item)
│   ├── schemas.py         # contratos de entrada e saída (Pydantic)
│   ├── rules/
│   │   └── dnd5e.py       # regras do jogo (lógica pura)
│   └── routers/           # endpoints agrupados por assunto
├── .env.example
├── requirements.txt
└── README.md
```

Arquivos como `models.py`, `schemas.py` e `routers/` aparecem à medida que as etapas do projeto avançam.

## Regras implementadas

As regras ficam isoladas em `app/rules/dnd5e.py`, sem dependência de banco ou de FastAPI:

| Cálculo | Regra |
|---|---|
| Modificador de atributo | `(valor - 10) // 2` |
| Bônus de proficiência | `2 + (nível - 1) // 4` |
| Perícia | modificador do atributo + proficiência (se tiver) |
| Teste de resistência | modificador do atributo + proficiência (se tiver) |
| Iniciativa | modificador de Destreza |
| Percepção passiva | `10 +` bônus da perícia Percepção |

## Roteiro de desenvolvimento

1. Setup e regras de D&D 5e
2. Configuração, banco de dados e modelos
3. CRUD de personagens e ficha calculada
4. Autenticação
5. Interface web
6. Deploy (Render + Neon)
7. Rolador de dados, busca de magias e compartilhamento por link

## Licença

Código distribuído sob a licença [MIT](LICENSE).

## Atribuição

Este trabalho inclui material do System Reference Document 5.1 ("SRD 5.1") da Wizards of the Coast LLC, disponível em <https://dnd.wizards.com/resources/systems-reference-document>. O SRD 5.1 é licenciado sob a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).

Nat20 é um projeto independente, sem afiliação com a Wizards of the Coast. Dungeons & Dragons é marca registrada da Wizards of the Coast LLC.