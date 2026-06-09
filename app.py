from flask import Flask
import psutil
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Coleta as métricas de hardware
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    
    # Cria uma estrutura HTML simples para exibir no navegador
    html = f"""
    <html>
        <head>
            <title>Monitor de Infraestrutura</title>
            <meta http-equiv="refresh" content="5"> <style>
                body {{ font-family: Arial, sans-serif; background: #f0f2f5; text-align: center; padding-top: 50px; }}
                .card {{ background: white; padding: 20px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 10px; min-width: 200px; }}
                h1 {{ color: #333; }}
                .porcentagem {{ font-size: 24px; font-weight: bold; color: #007bff; }}
            </style>
        </head>
        <body>
            <h1>🖥️ Monitor de Hardware ao Vivo</h1>
            <p>Este painel está rodando de dentro de um Container Docker!</p>
            
            <div class="card">
                <h3>Uso de Memória RAM</h3>
                <p class="porcentagem">{memoria}%</p>
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
    # O app vai rodar na porta 5000 e aceitar conexões de qualquer lugar (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)
