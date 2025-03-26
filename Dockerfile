# Usar imagem oficial do Python
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta da aplicação
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "run.py"]
