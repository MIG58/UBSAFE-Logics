import subprocess


def busb():
    # Define the script filename
    script_filename = "./blockusb.sh"

    # Run the chmod +x command on the script file
    chmod_command = ["sudo", "chmod", "+x", script_filename]

    try:
        subprocess.run(chmod_command, check=True)
        print(f"Successfully made {script_filename} executable.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to make {script_filename} executable. {e}")
