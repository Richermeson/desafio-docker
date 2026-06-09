from flask import Flask
import psutil
import os
import requests  # Importa a biblioteca para fazer envios para a internet

app = Flask(__name__)

# LER AS VARIÁVEIS DE AMBIENTE (Segurança)
# O Python vai tentar ler o link do Discord e o limite direto do sistema do Docker
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_URL")
LIMITE_MEMORIA = float(os.getenv("LIMITE_RAM", 50.0))  # Se não passarmos nada, o padrão é 50%

def enviar_alerta_discord(mensagem):
    """Função que pega um texto e chuta direto para o canal do Discord"""
    if DISCORD_WEBHOOK_URL:
        payload = {"content": mensagem}  # O Discord exige que o texto venha com a chave "content"
        try:
            # Faz uma requisição POST (envio de dados) para o link do Discord
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except Exception as e:
            print(f"Erro ao enviar para o Discord: {e}")

@app.route('/')
def home():
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    
    # Se a memória atual for maior que o limite configurado, envia o alerta!
    if memoria > LIMITE_MEMORIA:
        alerta = f"🚨 **ALERTA DE INFRAESTRUTURA** 🚨\nO uso de Memória RAM atingiu **{memoria}%**, ultrapassando o limite seguro de {LIMITE_MEMORIA}%!"
        enviar_alerta_discord(alerta)
    
    html = f"""
    <html>
        <head>
            <title>Monitor de Infraestrutura v2</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body {{ font-family: Arial, sans-serif; background: #2c3e50; text-align: center; padding-top: 50px; color: white; }}
                .card {{ background: #34495e; padding: 20px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.3); margin: 10px; min-width: 200px; }}
                .porcentagem {{ font-size: 24px; font-weight: bold; color: #e74c3c; }}
            </style>
        </head>
        <body>
            <h1>🖥️ Monitor de Hardware + Alertas v2</h1>
            <p>Monitorando e enviando alertas para o Discord!</p>
            
            <div class="card">
                <h3>Uso de Memória RAM</h3>
                <p class="porcentagem">{memoria}%</p>
                <p>Limite: {LIMITE_MEMORIA}%</p>
            </div>
            
            <div class="card">
                <h3>Uso de Disco</h3>
                <p class="porcentagem">{disco}%</p>
            </div>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
