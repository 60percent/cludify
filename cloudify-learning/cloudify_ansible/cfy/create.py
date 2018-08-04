import subprocess

command = '''
if ! [ -x "$(command -v terraform)" ]; then
    sudo yum install ansible --assumeyes --verbose
fi
'''
subprocess.check_call(command, shell=True)
