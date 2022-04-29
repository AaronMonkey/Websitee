import paramiko

switch_ip = "192.168.255.253"
switch_username = "admin"
switch_password = "admin"

ssh = paramiko.SSHClient()


def run_command_on_device(ip_address, username, password, command):
    """ Connect to a device, run a command, and return the output."""

    ssh.load_system_host_keys() #keys loaded 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #If needed add key function 

    total_attempts = 3
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt) #router connection 
            ssh.connect(switch_ip,
                        username=switch_username,
                        password=switch_password,
                        look_for_keys=False)
            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            # Read output from command.
            output = ssh_stdout.readlines()
            # Close connection.
            ssh.close()
            return output

        except Exception as error_message:
            print("Unable to connect")
            print(error_message)

print("Got to line 36")
# Run function
switch_output = run_command_on_device(
    switch_ip, switch_username, switch_password, "enable port 4")

# Analyze show ip route output
# Make sure we didn't receive empty output.
if switch_output != None:
    for line in switch_output:
        if 'str' in line:
            print("Default Line given:")
            print(line)
print("Finished program")