import subprocess


def sysbackup():
    bscripts = 'system_backup_restore/sysbackup.sh'
    subprocess.check_call(['sudo', 'sh', bscripts])
    print("System Backup Stated...! Please do not touch the Keyword")


def sysrestore():
    try:
        bscript = 'system_backup_restore/sysrestore.sh'
        subprocess.check_call(['sudo', 'bash', bscript])
        print("System Restore Stated...! Please do not touch the Keyword")

    except Exception as e:
        print("System Backup or Restore Error")
