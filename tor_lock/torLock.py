import subprocess


def tor_lock():
    try:
        bscript = 'tor_lock/torLock.sh'
        subprocess.check_call(['sudo', 'bash', bscript])
        print("Tor Locked..")

    except Exception as e:
        print("Tor Lock Error")
