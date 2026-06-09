FROM python:3.12-slim

WORKDIR /app

# Agora instalamos o psutil E também o flask
RUN pip install --no-cache-dir psutil flask

COPY app.py .

# Avisa o Docker que este container vai escutar na porta 5000
EXPOSE 5000

CMD ["python", "app.py"]
