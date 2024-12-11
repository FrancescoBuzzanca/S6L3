import socket
import random

def main():
    target_ip=input("inserisci IP della macchina target: ")

    try:
        target_port=int(input("inserisci la porta UPD della macchina target: "))
        if not (0<= target_port <= 65535):
            raise ValueError("porta non valida. deve essere compresa tra 0 e 655635")
    except ValueError as e:
        print(f"Errore: {e}")
        return 
    try:
        udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket UPD creato cpn successo")
    except socket.error as e:
        print(f"Errore nella creazione del socket: {e}")
        return
    packet_size= 1024
    try:
        num_packets=int(input("inserisci il numero di pacchetti da inviare: "))
        if num_packets<=0:
            raise ValueError("il numero di pacchetti deve essere maggiore di zero. ")
    except ValueError as e:
        print(f"Errore: {e}")
        return 
    for i in range(num_packets):
        packet=bytes(random.getrandbits(8) for _ in range(packet_size)) 
        try:
            udp_socket.sendto(packet, (target_ip, target_port))
            print(f"pacchetto {i+1}/{num_packets}inviato a {target_ip}:{target_port}")
        except Exception as e:
            print(f"Errore nell'invio del pacchetto {i+1}: {e}")
            break 
    udp_socket.close()
    print("programma terminato ")
if __name__=="__main__":
    main()
    
