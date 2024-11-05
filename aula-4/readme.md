# Ambiente Python para Desenvolvimento

- Após o download, dentro do [Visual Studio Code](https://code.visualstudio.com/), execute o comando para criar e utilizar o ambiente Python

  ```bash
  docker-compose up -d --build
  ```

## Visual Studio Code

> Caso já tenha o Visual Studio Code instalado em seu sistema operacional, não é necessário seguir os passos abaixo

Aqui estão as instruções para instalar o Visual Studio Code (VSCode) em diferentes sistemas operacionais.

### Windows

1. Acesse o site oficial do VSCode em [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Clique no botão de download para Windows.
3. Execute o instalador que foi baixado (geralmente chamado `VSCodeSetup.exe`).
4. Siga as instruções do instalador, aceitando os padrões recomendados, como associação de arquivos, a menos que você tenha preferências específicas.
5. Após a instalação, inicie o Visual Studio Code a partir do menu Iniciar ou do ícone na área de trabalho.

### macOS

1. Acesse o site oficial do VSCode em [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Clique no botão de download para macOS.
3. Uma vez que o arquivo `.dmg` for baixado, abra-o.
4. Arraste o ícone do Visual Studio Code para a pasta de "Aplicativos" no seu Mac.
5. Abra o VSCode a partir da pasta de "Aplicativos" ou da Dock.

### Linux

1. A forma mais simples de instalar o Visual Studio Code em distribuições Debian/Ubuntu é baixar e instalar o pacote `.deb` (64 bits) [Debian ou Ubuntu](https://code.visualstudio.com/download). Caso utilize outra distribuição, [neste link você encontra a documentação oficial com as explicações e passo a passo da instalação](https://code.visualstudio.com/docs/setup/linux).

---

## Configurando o FastAPI

Para adicionar o **FastAPI** ao seu ambiente, siga os passos abaixo:

### 1. Instale o FastAPI e o Uvicorn

No terminal do VSCode, instale as dependências com o seguinte comando:

```bash
pip install fastapi uvicorn
```

### 2. Crie um Arquivo de Exemplo com FastAPI

Crie um arquivo chamado `app.py` com o conteúdo a seguir para definir uma API simples:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
```

### 3. Execute o Servidor

Para iniciar o servidor, execute o comando abaixo:

```bash
uvicorn app:app --host 0.0.0.0 --port 4000 --reload
```

Isso iniciará o servidor FastAPI no endereço [http://0.0.0.0:4000](http://0.0.0.0:4000). Para ver a documentação interativa da API, acesse [http://0.0.0.0:4000/docs](http://0.0.0.0:4000/docs).

---

### 4. Verifique se o Docker está Configurado

Se você estiver utilizando o Docker para o ambiente de desenvolvimento, inclua o FastAPI no seu `Dockerfile` ou `docker-compose.yml` para garantir que ele seja iniciado automaticamente dentro do contêiner.

Exemplo para o `Dockerfile`:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]
```

Exemplo para o `docker-compose.yml`:

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "4000:4000"
    volumes:
      - .:/app
    command: uvicorn app:app --host 0.0.0.0 --port 4000 --reload
```