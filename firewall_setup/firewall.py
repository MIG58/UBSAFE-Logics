import subprocess


def fwall():
    try:
        bscript = 'firewall_setup/firewall.py'
        subprocess.check_call(['sudo', 'bash', bscript])
        print("Firewall setup successfully")

    except Exception as e:
        print("Unable to Setup Firewall")
