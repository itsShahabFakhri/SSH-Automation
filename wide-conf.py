import paramiko

usernames = []
hosts = []
passwords = []
conf_files = []

while True:
    inpUser = input("Username: ")
    if inpUser == "done":
        print("")
        break
    usernames.append(inpUser)
    inpHost = input("IP: ")
    hosts.append(inpHost)
    inpPassword = input("Password: ")
    passwords.append(inpPassword)
    inpConf = input("Configuration File Name: ")
    conf_files.append(inpConf)
    print("")

for i in range(len(usernames)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(hostname=hosts[i], username=usernames[i], password=passwords[i])
        with open(f"configuration_files/{conf_files[i]}", "r", encoding="utf-8") as f:
            for line in f:
                cmd = line.strip()
                if cmd:
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    print(stdout.read().decode(), end='')
        print(f"config for {usernames[i]}@{hosts[i]} done")
    except Exception as e:
        print(f"error on {usernames[i]}@{hosts[i]} -> {e}")
    
    ssh.close()

print(f"\nall done!\n")
