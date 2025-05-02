# 🛠 SSH Multi-Host Configurator Script

This is a **simple Python script** to automate running configuration commands over SSH on multiple hosts.

## ✅ Requirements

Make sure you have the following installed:

```
python3
pip install paramiko
```

---

## ⚙️ How It Works

Sometimes each host requires a different configuration, and sometimes the same config can be used across multiple hosts.

You need to:
- Create your configuration files as `.txt` files
- Put them inside the `configuration_files` directory
- Each line in the config file should be a command to run

When you run the script, it will ask for:
- Username
- IP address
- Password
- Config file name (from `configuration_files/` and only script name. ex: conf_mike.txt)

To stop adding new hosts, type `done` as the Username.

The script will then connect to each host and run the commands from the corresponding file.

---

## 💻 Example Usage

```bash
~/programming $ python3 wide-conf.py 
Username: mike
IP: 192.168.1.5
Password: 123456
Configuration File Name: conf_mike.txt

Username: Router-Os
IP: 192.168.1.100
Password: 87654321 
Configuration File Name: conf_mikrotik.txt

Username: ali  
IP: 185.62.36.21
Password: SfDe#df$fgW@122*y7     
Configuration File Name: conf_ali.txt

Username: done

config for mike@192.168.1.5 done  
config for Router-Os@192.168.1.100 done  
config for ali@185.62.36.21 done  

all done!
```

---

## 📂 Folder Structure

```
your-project/
│
├── wide-conf.py
├── configuration_files/
│   ├── conf_mike.txt
│   ├── conf_mikrotik.txt
│   └── conf_ali.txt
```

---

## 🔒 Security Note

This script handles plaintext passwords and sends them over SSH. Make sure you're using it in **trusted environments only**, and avoid storing sensitive credentials in source code or shared folders.
