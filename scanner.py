import socket
from datetime import datetime

def port_scan(target):
    print("-" * 50)
    print(f"Сканирование цели: {target}")
    print(f"Время запуска: {datetime.now()}")
    print("-" * 50)
    
    # Проверяем порты от 1 до 1024
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Порт {port}: ОТКРЫТ")
        s.close()

if __name__ == "__main__":
    target_ip = input("Введите IP-адрес или домен: ")
    port_scan(target_ip)
