# 1. Usa uma imagem oficial do Python como base
FROM python:3.12-slim

# 2. Define a pasta de trabalho dentro do container
WORKDIR /app

# 3. Instala a biblioteca psutil direto no sistema do container
RUN pip install --no-cache-dir psutil

# 4. Copia o seu script app.py para dentro do container
COPY app.py .

# 5. Comando para executar o monitor assim que o container subir
CMD ["python", "app.py"]
