# Projeto de Backend com Python, Django, FastAPI e Docker

Este repositório contém um projeto backend desenvolvido como parte das aulas do MBA em Engenharia de Software da USP. O projeto utiliza **Python**, **Django**, **FastAPI**, e **Docker**, seguindo as práticas recomendadas para desenvolvimento de APIs RESTful e serviços rápidos, com deploy em contêineres.

## 📋 Descrição do Projeto

Este projeto é um sistema backend completo, construído com os frameworks **Django** e **FastAPI**, integrados a um banco de dados e preparados para execução em um ambiente **Dockerizado**. O objetivo é proporcionar experiência tanto em desenvolvimento com Django quanto com FastAPI, oferecendo flexibilidade para construir APIs síncronas e assíncronas, com foco em escalabilidade e facilidade de deploy.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação para o desenvolvimento backend.
- **Django**: Framework web para construção de APIs RESTful e gerenciamento de rotas.
- **FastAPI**: Framework rápido e assíncrono, ideal para endpoints de alta performance.
- **Docker**: Ferramenta para criação de contêineres, facilitando a implantação do ambiente.
- **Docker Compose**: Para orquestrar múltiplos contêineres (aplicação e banco de dados).
- **PostgreSQL**: Banco de dados relacional integrado ao projeto via contêiner.

## 🚀 Funcionalidades

- [ ] CRUD de exemplo (Criação, Leitura, Atualização e Exclusão) com Django e FastAPI.
- [ ] Endpoints para gerenciamento de recursos da aplicação.
- [ ] Autenticação básica e (opcional) Autenticação JWT com FastAPI.
- [ ] Integração com banco de dados PostgreSQL em contêiner Docker.

## 📦 Estrutura do Projeto

```
├── app/
│   ├── Dockerfile           # Dockerfile para configurar o contêiner da aplicação
│   ├── manage.py            # Arquivo principal do Django
│   ├── requirements.txt     # Dependências do projeto
│   ├── settings.py          # Configurações do Django
│   ├── fastapi_app/         # Pasta para endpoints e configurações do FastAPI
│   │   ├── main.py          # Arquivo principal do FastAPI
│   │   └── ...
├── docker-compose.yml       # Configuração para orquestrar os contêineres
└── README.md                # Documentação do projeto
```

## ⚙️ Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- **Docker**: [Instalar Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```

2. Configure o arquivo `docker-compose.yml` caso seja necessário (banco de dados, variáveis de ambiente etc.).

3. Suba o ambiente com Docker Compose:

   ```bash
   docker-compose up -d
   ```

4. Acesse a aplicação Django no navegador em `http://localhost:8000` (ou outra porta configurada no `docker-compose.yml`) e a aplicação FastAPI na URL `http://localhost:8001/docs`, onde a documentação interativa estará disponível.

5. Para ver os logs dos contêineres:

   ```bash
   docker-compose logs -f
   ```

6. Para encerrar os contêineres:

   ```bash
   docker-compose down
   ```

## 📝 Comandos Úteis

- **Criar Migrações com Django**:

  ```bash
  docker-compose run app python manage.py makemigrations
  ```

- **Aplicar Migrações com Django**:

  ```bash
  docker-compose run app python manage.py migrate
  ```

- **Criar Superusuário para o Django Admin**:

  ```bash
  docker-compose run app python manage.py createsuperuser
  ```

- **Iniciar FastAPI**: O FastAPI inicia automaticamente ao rodar o `docker-compose up`, mas para rodar localmente, use:

  ```bash
  uvicorn fastapi_app.main:app --reload
  ```

## 📝 Configuração de Endpoints no FastAPI

O arquivo `fastapi_app/main.py` é onde você poderá adicionar novos endpoints de forma assíncrona, usando a estrutura padrão do FastAPI. Acesse a documentação gerada automaticamente em `http://localhost:8001/docs`.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.