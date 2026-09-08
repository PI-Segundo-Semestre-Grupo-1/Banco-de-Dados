import mysql.connector as m
import psutil as p
import time 
from datetime import datetime

conexao = m.connect(
    host="127.0.0.1",
    user="aluno",
    password="Jo142365879*",
    database="magnasync_rm",
    use_pure=True
)

cursor = conexao.cursor()

#Horario
horario_exibicao = datetime.now().strftime("%y-%m-%d %H:%M:%S")


# CPU
perc_cpu = p.cpu_percent(interval=1)
freq_cpu = p.cpu_freq().current
nucleos = p.cpu_count()

# memoria
uso = p.virtual_memory().percent
memoria_total = p.virtual_memory().total / (1024 ** 3)
memoria_disponivel = p.virtual_memory().available / (1024 ** 3)

# disco
uso_disco = p.disk_usage('/').percent
espaço_total = p.disk_usage('/').total / (1024 ** 3)
espaço_disponivel = p.disk_usage('/').free / (1024 ** 3)

# redes
velocidade = p.net_if_stats()["Wi-Fi"].speed
meu_ip = p.net_if_addrs()["Wi-Fi"][1].address
esta_ativa = p.net_if_stats()["Wi-Fi"].isup
wifi_status = "Ativo" if esta_ativa else "Inativo"
#print(f"Wi-Fi Ativo: {esta_ativa} | IP: {meu_ip} | Velocidade: {velocidade} Mbps")

#Discretização
#CPU
if perc_cpu < 70:
    status_cpu = "NORMAL"
elif perc_cpu < 90:
    status_cpu = "ALERTA"
else:
    status_cpu = "CRITICO"

#Frequência da CPU
freq_maxima = p.cpu_freq().max
if freq_cpu >= freq_maxima * 0.80:
    status_frequencia = "NORMAL"
elif freq_cpu >= freq_maxima * 0.60:
    status_frequencia = "ALERTA"
else:
    status_frequencia = "CRITICO"

#Nucléos
if nucleos >= 4:
    status_nucleos = "NORMAL"
elif nucleos >= 2:
    status_nucleos = "ALERTA"
else:
    status_nucleos = "CRITICO"

# Memória
if uso < 75:
    status_memoria = "NORMAL"
elif uso < 90:
    status_memoria = "ALERTA"
else:
    status_memoria = "CRITICO"

#percentual memoria
percentual_disponivel = 100 - uso
if percentual_disponivel > 25:
    status_memoria_disponivel = "NORMAL"
elif percentual_disponivel >= 10:
    status_memoria_disponivel = "ALERTA"
else:
    status_memoria_disponivel = "CRITICO"

# Disco
if uso_disco < 75:
    status_disco = "NORMAL"
elif uso_disco < 90:
    status_disco = "ALERTA"
else:
    status_disco = "CRITICO"

#Percentual Disco
percentual_disco_disponivel = 100 - uso_disco
if percentual_disco_disponivel > 25:
    status_espaco_disponivel = "NORMAL"
elif percentual_disco_disponivel >= 10:
    status_espaco_disponivel = "ALERTA"
else:
    status_espaco_disponivel = "CRITICO"

# Rede
if esta_ativa:
    status_rede = "NORMAL"
elif not esta_ativa:
    status_rede = "CRITICO"

#Velocidade    
if velocidade >= 100:
    status_velocidade = "NORMAL"
elif velocidade >= 50:
    status_velocidade = "ALERTA"
else:
    status_velocidade = "CRITICO"


print("\nStatus da Maquina De Ressonancia Magnética")
print(f"CPU: {perc_cpu}% | {status_cpu}")
print(f"Frequência: {freq_cpu} MHz | {status_frequencia}")
print(f"Núcleos: {nucleos} | {status_nucleos}")
print(f"Memória: {uso}% | {status_memoria}")
print(f"Memória disponível: {memoria_disponivel:.2f} GB | {status_memoria_disponivel}")
print(f"Disco: {uso_disco}% | {status_disco}")
print(f"Espaço disponível: {espaço_disponivel:.2f} GB | {status_espaco_disponivel}")
print(f"Rede Wi-Fi: {wifi_status} | {status_rede}")
print(f"Velocidade da rede: {velocidade} Mbps | {status_velocidade}")
print("---------------------------------------------------------")

# inserts
insert = "INSERT INTO registroCpu (id_equipamento, percentual_uso, frequencia, nucleos, data_hora) VALUES (%s, %s, %s, %s, %s)"
dados = (1, perc_cpu, freq_cpu, nucleos, horario_exibicao)

insert2 = "INSERT INTO registroRam (id_equipamento, percentual_uso, memoria_total, memoria_disponivel, data_hora) VALUES (%s, %s, %s, %s, %s)"
dados2 = (1, uso, memoria_total, memoria_disponivel, horario_exibicao)

insert3 = "INSERT INTO registroArmazenamento (id_equipamento, percentual_uso, espaco_total, espaco_disponivel, data_hora) VALUES (%s, %s, %s, %s, %s)"
dados3 = (1, uso_disco, espaço_total, espaço_disponivel, horario_exibicao)

insert4 = "INSERT INTO registroRedes (id_equipamento, wifi_ativo, ip_rede, velocidade, data_hora) VALUES (%s, %s, %s, %s, %s)"
dados4 = (1, wifi_status, meu_ip, velocidade, horario_exibicao)

cursor.execute(insert, dados)
cursor.execute(insert2, dados2)
cursor.execute(insert3, dados3)
cursor.execute(insert4, dados4)

conexao.commit()

print("Dados capturados e inseridos com sucesso!")

cursor.close()
conexao.close()