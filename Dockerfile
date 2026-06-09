FROM python:3.12-slim

WORKDIR /app

# Adicionamos o 'requests' na lista de instalação do pip
RUN pip install --no-cache-dir psutil flask requests

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
