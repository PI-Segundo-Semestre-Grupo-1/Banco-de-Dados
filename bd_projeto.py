import mysql.connector as m

conexao = m.connect(
    host="",
    user="",
    password="",
    database="",
)

cursor = conexao.cursor()

while True:

    print("MENU")
    print("\n1 - Ver todos os dados")
    print("2 - Ver CPU")
    print("3 - Ver memória")
    print("4 - Ver disco")
    print("5 - Ver redes")
    print("6 - Ver timestamp e percentual de CPU")
    print("7 - Ver timestamp e percentual de memória")
    print("8 - Ver timestamp e se a rede está ativa")
    print("9 - Ver timestamp e percentual de disco")
    print("10 - Deletar os ultimos 5 registros")
    print("11 - Atualizar os 3 últimos registros para a data atual")
    print("12 - Sair")
    print("-----------------------------")

    opcao = input("Digite o que você quer: ")


    if opcao == "1":

        print("\nCPU")

        comando = "SELECT id_equipamento, percentual_uso, frequencia, nucleos, data_hora FROM registroCpu"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        for linha in resultados:

            if linha[1] < 70:
                status_cpu = "NORMAL"
            elif linha[1] < 90:
                status_cpu = "ALERTA"
            else:
                status_cpu = "CRITICO"

            print(f"ID: {linha[0]} | CPU: {linha[1]}% | Frequência: {linha[2]} MHz | Núcleos: {linha[3]} | Timestamp: {linha[4]} | Status CPU: {status_cpu}")

        print("\nMemória")

        comando = "SELECT id_equipamento, percentual_uso, memoria_total, memoria_disponivel, data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        for linha in resultados:

            if linha[1] < 75:
                status_memoria = "NORMAL"
            elif linha[1] < 90:
                status_memoria = "ALERTA"
            else:
                status_memoria = "CRITICO"

            percentual_disponivel = 100 - linha[1]

            if percentual_disponivel > 25:
                status_memoria_disponivel = "NORMAL"
            elif percentual_disponivel >= 10:
                status_memoria_disponivel = "ALERTA"
            else:
                status_memoria_disponivel = "CRITICO"

            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]} | Status Memória Uso: {status_memoria} | Status Memória Disponível: {status_memoria_disponivel}")

        print("\nDisco")

        comando = "SELECT id_equipamento, percentual_uso, espaco_total, espaco_disponivel, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        for linha in resultados:

            if linha[1] < 75:
                status_disco = "NORMAL"
            elif linha[1] < 90:
                status_disco = "ALERTA"
            else:
                status_disco = "CRITICO"

            percentual_disco_disponivel = 100 - linha[1]

            if percentual_disco_disponivel > 25:
                status_espaco_disponivel = "NORMAL"
            elif percentual_disco_disponivel >= 10:
                status_espaco_disponivel = "ALERTA"
            else:
                status_espaco_disponivel = "CRITICO"

            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]} | Status Disco Uso: {status_disco} | Status Disco Espaço Disponível: {status_espaco_disponivel}")

        print("\nRedes")

        comando = "SELECT id_equipamento, wifi_ativo, ip_rede, velocidade, data_hora FROM registroRedes"
                        
        cursor.execute(comando)
        resultados = cursor.fetchall()
                               
        for linha in resultados:
                        
                if linha[1] == "Ativo":
                    status_rede = "NORMAL"
                elif linha[1] == "Inativo":
                    status_rede = "CRITICO"
                else:
                    status_rede = "CRITICO"
            
                if linha[3] is None:
                    status_velocidade = "CRITICO"
                elif linha[3] >= 100:
                    status_velocidade = "NORMAL"
                elif linha[3] >= 50:
                    status_velocidade = "ALERTA"
                else:
                    status_velocidade = "CRITICO"
                        
                print(f"ID: {linha[0]} | Wi-Fi Ativo: {linha[1]} | IP: {linha[2]} | Velocidade: {linha[3]} Mbps | Status Rede: {status_rede} | Status Velocidade Rede: {status_velocidade}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "2":

        comando = "SELECT id_equipamento, percentual_uso, frequencia, nucleos, data_hora FROM registroCpu"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nCPU")

        for linha in resultados:

            if linha[1] < 70:
                status_cpu = "NORMAL"
            elif linha[1] < 90:
                status_cpu = "ALERTA"
            else:
                status_cpu = "CRITICO"

            if linha[3] is None:
                status_nucleos = "NORMAL"
            elif linha[3] >= 2:
                status_nucleos = "ALERTA"
            else:
                status_nucleos = "CRITICO"

            print(f"ID: {linha[0]} | CPU: {linha[1]}% | Frequência: {linha[2]} MHz | Núcleos: {linha[3]} | Timestamp: {linha[4]} | Status CPU: {status_cpu} | Status Núcleos CPU: {status_nucleos}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":

        comando = "SELECT id_equipamento, percentual_uso, memoria_total, memoria_disponivel, data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nMemória")

        for linha in resultados:

            if linha[1] < 75:
                status_memoria = "NORMAL"
            elif linha[1] < 90:
                status_memoria = "ALERTA"
            else:
                status_memoria = "CRITICO"

            percentual_disponivel = 100 - linha[1]

            if percentual_disponivel > 25:
                status_memoria_disponivel = "NORMAL"
            elif percentual_disponivel >= 10:
                status_memoria_disponivel = "ALERTA"
            else:
                status_memoria_disponivel = "CRITICO"

            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]} | Status Memória Uso: {status_memoria} | Status Memória Disponível: {status_memoria_disponivel}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "4":

        comando = "SELECT id_equipamento, percentual_uso, espaco_total, espaco_disponivel, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nDisco")

        for linha in resultados:

            if linha[1] < 75:
                status_disco = "NORMAL"
            elif linha[1] < 90:
                status_disco = "ALERTA"
            else:
                status_disco = "CRITICO"

            percentual_disco_disponivel = 100 - linha[1]

            if percentual_disco_disponivel > 25:
                status_espaco_disponivel = "NORMAL"
            elif percentual_disco_disponivel >= 10:
                status_espaco_disponivel = "ALERTA"
            else:
                status_espaco_disponivel = "CRITICO"

            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]} | Status Disco Uso: {status_disco} | Status Disco Espaço Disponível: {status_espaco_disponivel}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "5":
            
        comando = "SELECT id_equipamento, wifi_ativo, ip_rede, velocidade, data_hora FROM registroRedes"
            
        cursor.execute(comando)
        resultados = cursor.fetchall()
            
        print("\nRedes")
            
        for linha in resultados:

            if linha[1] == "Ativo":
                status_rede = "NORMAL"
            elif linha[1] == "Inativo":
                status_rede = "CRITICO"
            else:
                status_rede = "CRITICO"

        if linha[3] is None:
            status_velocidade = "CRITICO"
        elif linha[3] >= 100:
            status_velocidade = "NORMAL"
        elif linha[3] >= 50:
            status_velocidade = "ALERTA"
        else:
            status_velocidade = "CRITICO"
            
        print(f"ID: {linha[0]} | Wi-Fi Ativo: {linha[1]} | IP: {linha[2]} | Velocidade: {linha[3]} Mbps | Status Rede: {status_rede} | Status Velocidade Rede: {status_velocidade}")

        input("\nPressione ENTER para voltar ao menu...")
            
    elif opcao == "6":

        comando = "SELECT percentual_uso, data_hora FROM registroCpu"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + CPU")

        for linha in resultados:

            if linha[0] < 70:
                status_cpu = "NORMAL"
            elif linha[0] < 90:
                status_cpu = "ALERTA"
            else:
                status_cpu = "CRITICO"

            print(f"CPU: {linha[0]}% | Timestamp: {linha[1]} | Status CPU: {status_cpu}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "7":

        comando = "SELECT percentual_uso, data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + Memória")

        for linha in resultados:

            if linha[0] < 75:
                status_memoria = "NORMAL"
            elif linha[0] < 90:
                status_memoria = "ALERTA"
            else:
                status_memoria = "CRITICO"

            print(f"Memória: {linha[0]}% | Timestamp: {linha[1]} | Status Memória: {status_memoria}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "8":
    
        comando = "SELECT wifi_ativo, data_hora FROM registroRedes"
    
        cursor.execute(comando)
        resultados = cursor.fetchall()
    
        print("\nTimestamp + Wi-fi")
    
        for linha in resultados:
            status_rede = ""

            if linha[0] == "Ativo":
                status_rede = "NORMAL"
            elif linha[0] == "Inativo":
                status_rede = "CRITICO"
    
            print(f"Wi-Fi Ativo: {linha[0]} | Timestamp: {linha[1]} | Status Rede: {status_rede}")
    
        input("\nPressione ENTER para voltar ao menu...")
    
    elif opcao == "9":

        comando = "SELECT percentual_uso, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + Disco")

        for linha in resultados:

            if linha[0] < 75:
                status_disco = "NORMAL"
            elif linha[0] < 90:
                status_disco = "ALERTA"
            else:
                status_disco = "CRITICO"

            print(f"Disco: {linha[0]}% | Timestamp: {linha[1]} | Status Disco: {status_disco}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "10":
                
        print("\nDeletando os 5 ultimos registros...")
                
        comando = "DELETE FROM registroCpu ORDER BY id_cpu DESC LIMIT 5"
        cursor.execute(comando)

        comando = "DELETE FROM registroRam ORDER BY id_ram DESC LIMIT 5"
        cursor.execute(comando)

        comando = "DELETE FROM registroArmazenamento ORDER BY id_armazenamento DESC LIMIT 5"
        cursor.execute(comando)

        comando = "DELETE FROM registroRedes ORDER BY id_rede DESC LIMIT 5"
        cursor.execute(comando)
        
                
        conexao.commit()
                
        print("Os 5 últimos registros foram deletados.")

        input("\nPressione ENTER para voltar ao menu...")
    
    elif opcao == "11":
    
        print("\nAtualizando os 3 ultimos registros...")
    
        comando = "UPDATE registroCpu SET data_hora = NOW() ORDER BY id_cpu DESC LIMIT 3"
        cursor.execute(comando)

        comando = "UPDATE registroRam SET data_hora = NOW() ORDER BY id_ram DESC LIMIT 3"
        cursor.execute(comando)

        comando = "UPDATE registroArmazenamento SET data_hora = NOW() ORDER BY id_armazenamento DESC LIMIT 3"
        cursor.execute(comando)

        comando = "UPDATE registroRedes SET data_hora = NOW() ORDER BY id_rede DESC LIMIT 3"
        cursor.execute(comando)
    
        conexao.commit()
    
        print("Os 3 últimos registros foram atualizados para a data atual.")

        input("\nPressione ENTER para voltar ao menu...")
            
    elif opcao == "12":

        print("\nEncerrando programa...")
        break

    else:
        print("\nOpção invalida digite um numero de 1 a 12.")


cursor.close()
conexao.close()
