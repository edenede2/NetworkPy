import paramiko
from rich import print
import time
import re

host = '132.74.68.175'
user = 'psylab-6028'
password = '8X-Zpp()'

# Function to clean output by removing terminal control sequences
def clean_output(output):
    # Remove ANSI escape sequences and control characters
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])|(?:\x1b\[.*?[@-~])')
    return ansi_escape.sub('', output)

def run_command_real_time(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=port, username=username, password=password)

    channel = ssh.invoke_shell()
    time.sleep(1)  # Allow time for initial connection messages

    # Clear any welcome messages or prompts
    if channel.recv_ready():
        output = clean_output(channel.recv(1024).decode('utf-8'))
        print(output, end="")

    print("[bold green]Interactive SSH session started. Type 'exit' to close.[/bold green]")

    while True:
        command = input("ssh> ")

        if command.lower() == "exit":
            print("[bold red]Closing session...[/bold red]")
            break

        # Send command to the SSH session
        channel.send(command + "\n")

        # Wait for command output and clean it
        time.sleep(0.5)  # Slight delay for command processing
        output = ""
        while channel.recv_ready():
            output += channel.recv(4096).decode('utf-8')
            time.sleep(0.1)  # Prevent excessive CPU usage

        # Clean and print the server's output only
        print("\n" + clean_output(output), end="")

    ssh.close()


run_command_real_time(
    hostname=host,
    port=22,  
    username=user,
    password=password
)