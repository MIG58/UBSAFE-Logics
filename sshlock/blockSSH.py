import subprocess

def assh():
    # SSH Activate Script
    bscripts = 'sshlock/activessh.sh'
    subprocess.check_call(['sudo', 'sh', bscripts])
    print("SSH is Activated")

def bssh(): 
    try:

        # Use subprocess to run the Bash script with sudo
        # subprocess.check_call(['sudo', 'bash', bash_script_path])
        # BLOCK SSH Script
        bscript = 'sshlock/blockssh.sh'
        subprocess.check_call(['sudo', 'bash', bscript])
        print("SSH Blocked Successfully.")

    except Exception as e:
        print("SSH Blocked Successfully with some error 2.")
        
        # print("SSH is Blocked, Error occured")

