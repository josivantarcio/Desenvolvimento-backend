# Projeto de Backend com Python, Django e Docker

Este repositório contém um projeto backend desenvolvido como parte das aulas do MBA em Engenharia de Software da USP. O projeto utiliza **Python**, **Django** e **Docker**, seguindo as práticas recomendadas para desenvolvimento de APIs RESTful com deploy em contêineres.

## 📋 Descrição do Projeto

Este projeto é um sistema básico de backend construído com o framework **Django**, com integração a um banco de dados, e preparado para ser executado em um ambiente **Dockerizado**. O objetivo é desenvolver habilidades em desenvolvimento backend e automação de ambientes de execução, com foco em escalabilidade e facilidade de deploy.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação para o desenvolvimento backend.
- **Django**: Framework web para construção de APIs e gerenciamento de rotas.
- **Docker**: Ferramenta para criação de contêineres, facilitando a implantação do ambiente.
- **Docker Compose**: Para orquestrar múltiplos contêineres (como aplicação e banco de dados).

## 🚀 Funcionalidades

- [ ] CRUD de exemplo (Criação, Leitura, Atualização e Exclusão).
- [ ] Endpoints para gerenciamento de recursos da aplicação.
- [ ] Autenticação básica (opcional: Autenticação JWT).
- [ ] Integração com banco de dados PostgreSQL em contêiner Docker.
  
## 📦 Estrutura do Projeto

```
├── app/
│   ├── Dockerfile           # Dockerfile para configurar o contêiner da aplicação
│   ├── manage.py            # Arquivo principal do Django
│   ├── requirements.txt     # Dependências do projeto
│   ├── settings.py          # Configurações do Django
│   └── ...
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

4. Acesse a aplicação no navegador em `http://localhost:8000` (ou outra porta configurada no `docker-compose.yml`).

5. Para ver os logs dos contêineres:

   ```bash
   docker-compose logs -f
   ```

6. Para encerrar os contêineres:

   ```bash
   docker-compose down
   ```

## 📝 Comandos Úteis

- **Criar Migrações**:

  ```bash
  docker-compose run app python manage.py makemigrations
  ```

- **Aplicar Migrações**:

  ```bash
  docker-compose run app python manage.py migrate
  ```

- **Criar Superusuário para o Django Admin**:

  ```bash
  docker-compose run app python manage.py createsuperuser
  ```

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
