# Utilize a imagem do Python
FROM python:3.10

# Defina o diretório de trabalho no container
WORKDIR /app

# Instale o Poetry
RUN pip install poetry

# Copie apenas os arquivos necessários para instalar as dependências
COPY pyproject.toml poetry.lock* /app/

# Exporte as dependências para um requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do seu projeto
COPY . /app
