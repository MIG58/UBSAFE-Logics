import subprocess


def busb():
    try:
        script_path = 'blockusb/blockusb.sh'
        subprocess.run(['sudo', 'chmod', '+x', script_path], check=True)
        # Run the blockusb.sh script using subprocess
        subprocess.run("blockusb/blockusb.sh", check=True, shell=True)
        print("blockusb.sh script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing blockusb.sh script. Return code: {e.returncode}")
        print(e.output)

# Call the function to execute the script
# busb()

def ubusb():
    try:
        script_path = 'blockusb/ublockusb.sh'
        subprocess.run(['sudo', 'chmod', '+x', script_path], check=True)
        # Run the ublockusb.sh script using subprocess
        subprocess.run("blockusb/ublockusb.sh",check=True, shell=True)
        print("ublockusb.sh script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing ublockusb.sh script. Return code: {e.returncode}")
        print(e.output)

ubusb()

