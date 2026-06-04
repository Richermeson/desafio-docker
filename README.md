# 🖥️ Monitor de Hardware Conteinerizado

Este é um agente de telemetria e monitoramento de infraestrutura desenvolvido em Python e isolado utilizando Docker. O projeto coleta métricas de uso de memória RAM e Disco do sistema operacional e salva em arquivos de log persistentes.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12** (Lógica do script)
* **Psutil** (Biblioteca para coleta de métricas de hardware)
* **Docker** (Conteinerização e isolamento do ambiente)
* **Docker Volumes** (Persistência dos logs na máquina real)

## 🚀 Como Executar o Projeto

Se você esquecer os comandos, basta rodar este passo a passo no terminal:

```bash
# 1. Construir a imagem Docker
docker build -t meu-monitor-hardware .

# 2. Rodar o container em background com persistência de logs
docker run -d -e PYTHONUNBUFFERED=1 -v $(pwd):/app --name monitor_infra meu-monitor-hardware

# 3. Monitorar os logs em tempo real
tail -f alerta_uso.log
