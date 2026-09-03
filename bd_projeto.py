import mysql.connector as m

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
    print("8 - Ver timestamp e percentual de disco")
    print("9 - Ver timestamp e se a rede está ativa")
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
            print(f"ID: {linha[0]} | CPU: {linha[1]}% | Frequência: {linha[2]} MHz | Núcleos: {linha[3]} | Timestamp: {linha[4]}")

        print("\nMemória")

        comando = "SELECT id_equipamento, percentual_uso, memoria_total, memoria_disponivel, data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        for linha in resultados:
            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]}")

        print("\nDisco")

        comando = "SELECT id_equipamento, percentual_uso, espaco_total, espaco_disponivel, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        for linha in resultados:
            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "2":

        comando = "SELECT id_equipamento, percentual_uso, frequencia, nucleos, data_hora FROM registroCpu"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nCPU")
        for linha in resultados:
            print(f"ID: {linha[0]} | CPU: {linha[1]}% | Frequência: {linha[2]} MHz | Núcleos: {linha[3]} | Timestamp: {linha[4]}")
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":

        comando = "SELECT id_equipamento, percentual_uso, memoria_total, memoria_disponivel, data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nMemória")

        for linha in resultados:
            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "4":

        comando = "SELECT id_equipamento, percentual_uso, espaco_total, espaco_disponivel, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nDisco")

        for linha in resultados:
            print(f"ID: {linha[0]} | Uso: {linha[1]}% | Total: {linha[2]:.2f} GB | Disponível: {linha[3]:.2f} GB | Timestamp: {linha[4]}")
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "5":
            
                    comando = "SELECT id_equipamento, wifi_ativo, ip_rede, velocidade, data_hora FROM registroRedes"
            
                    cursor.execute(comando)
                    resultados = cursor.fetchall()
            
                    print("\nRedes")
            
                    for linha in resultados:
                        print(f"ID: {linha[0]} | :Wi-Fi Ativo: {linha[1]} | IP: {linha[2]} | Velocidade: {linha[3]} Mbps")
                    input("\nPressione ENTER para voltar ao menu...")
            
    elif opcao == "6":

        comando = "SELECT percentual_uso, data_hora FROM registroCpu"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + CPU")

        for linha in resultados:
            print(f"CPU: {linha[0]} | Timestamp: {linha[1]}%")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "7":

        comando = "SELECT percentual_uso ,data_hora FROM registroRam"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + Memória")

        for linha in resultados:
            print(f"Memória: {linha[0]} | Timestamp: {linha[1]}%")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "8":
    
        comando = "SELECT wifi_ativo, data_hora FROM registroRedes"
    
        cursor.execute(comando)
        resultados = cursor.fetchall()
    
        print("\nTimestamp + Wi-fi")
    
        for linha in resultados:
            print(f"Wifi ativo: {linha[0]} | Timestamp: {linha[1]}%")
    
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "9":

        comando = "SELECT percentual_uso, data_hora FROM registroArmazenamento"

        cursor.execute(comando)
        resultados = cursor.fetchall()

        print("\nTimestamp + Disco")

        for linha in resultados:
            print(f"Disco: {linha[0]} | Timestamp: {linha[1]}%")

        input("\nPressione ENTER para voltar ao menu...")

    


    elif opcao == "10":
                
        print("\nDeletando os 5 ultimos registros...")
                
        comando = "DELETE FROM registroCpu ORDER BY id_cpu DESC LIMIT 5"
        cursor.execute(comando)
        comando = "DELETE FROM registroRam ORDER BY id_ram DESC LIMIT 5"
        cursor.execute(comando)
        comando = "DELETE FROM registroArmazenamento ORDER BY id_armazenamento DESC LIMIT 5"
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
