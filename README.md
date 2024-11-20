 🔐 **KeyCracker**  
**Advanced SSH Brute Forcing Tool**  
_Crafted by [davycipher](https://github.com/cypherdavy)_

---

## 📜 **Introduction**  
KeyCracker is a powerful and efficient multi-threaded SSH brute-forcing tool designed for ethical penetration testing and cybersecurity awareness. With features like threading and a robust connection-handling mechanism, it makes testing SSH security a seamless process.

> ⚠️ **Disclaimer**: This tool is intended for educational and authorized penetration testing purposes only. Unauthorized use is illegal and unethical. Use responsibly.  

---

## 🚀 **Features**  
- **Multi-threading** for faster brute-forcing.  
- **Customizable SSH ports** and wordlist inputs.  
- Elegant and informative outputs for successes and failures.  
- Lightweight and easy to use.  
- Developed with a hacker-friendly aesthetic.  

---

## 🖥️ **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/cypherdavy/KeyCracker.git
   cd KeyCracker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python keycracker.py
   ```

---

## ⚙️ **Usage**  
```bash
python keycracker.py
```

### Input Details:
1. **Target IP Address**: The IP of the SSH server you want to test.  
2. **Username**: Username of the target system.  
3. **Wordlist**: Path to your password wordlist file.  
4. **Port** (optional): SSH port (default is `22`).  
5. **Threads** (optional): Number of threads for multi-threading (default is `5`).  

---

## 🌟 **Features in Action**  

```plaintext
      _  __           ____                _             
     | |/ /___ _   _ / ___|_ __ __ _  ___| | _____ _ __ 
     | ' // _ \ | | | |   | '__/ _` |/ __| |/ / _ \ '__|
     | . \  __/ |_| | |___| | | (_| | (__|   <  __/ |   
     |_|\_\___|\__, |\____|_|  \__,_|\___|_|\_\___|_|   
               |___/                                    

      Advanced SSH Brute Forcing Tool
                   Made by davycipher

Enter the IP address to brute force: 192.168.1.100
Enter the username for the target system: admin
Enter the path to the wordlist: wordlist.txt
Enter the SSH port (default 22): 
Enter the number of threads (default 5): 
[INFO] Target: 192.168.1.100:22
[INFO] Starting brute force attack...
[SUCCESS] Username: admin | Password: supersecure123
[INFO] Attack completed successfully.
```

---

## 🤖 **How It Works**  
1. **Password Queueing**: Reads passwords from a wordlist and adds them to a queue.  
2. **Threaded Attack**: Multiple threads attempt logins simultaneously for faster results.  
3. **Success Handling**: Stops the attack immediately upon finding valid credentials.  

---

## 🛠️ **Contribution**  
We welcome contributions! Feel free to submit issues or pull requests to enhance the tool.  

1. Fork the repository.  
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Push your branch and submit a pull request.  

---

## 📜 **License**  
This project is licensed under the [MIT License](LICENSE).

---

## 💬 **Contact**  
Feel free to reach out with feedback, questions, or ideas:  

- **Author**: David P.S. Abraham (a.k.a. [davycipher](https://github.com/cypherdavy))  
- **Email**: [davycypher@gmail.com](mailto:davycypher@gmail.com)  
- **Website**: [davycipher.online](https://davycipher.online)  

---

🌟 **Star the repository if you find this tool useful!**  
