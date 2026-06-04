import time
import psutil
from datetime import datetime

print("=== Sistema de Monitoramento Iniciado ===")

while True:
    # Coleta a porcentagem de uso e o horário atual
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    linha_log = f"[{agora}] RAM: {uso_ram}% | Disco: {uso_disco}%\n"
    
    # Printa na tela (para o docker logs continuar funcionando)
    print(linha_log.strip())
    
    # Salva e anexa (append) a informação dentro do arquivo de log
    with open("alerta_uso.log", "a") as arquivo:
        arquivo.write(linha_log)
        
    # Aguarda 5 segundos
    time.sleep(5)
