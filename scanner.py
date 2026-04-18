import socket

def port_scanner(host, ports):
    print(f"Escaneando {host}...")
    for port in ports:
        # Crea un socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Tiempo de espera para evitar bloqueos largos
        # connect_ex devuelve 0 si la conexión fue exitosa (puerto abierto)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Puerto {port} abierto")
        s.close()

target = "127.0.0.1" # Cambia por tu objetivo
ports_to_scan = range(1, 1025) # Escanea los puertos más comunes
port_scanner(target, ports_to_scan)
