import mysql.connector as m
import psutil as p
import time 
from datetime import datetime

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
