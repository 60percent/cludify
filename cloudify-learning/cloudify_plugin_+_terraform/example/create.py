import subprocess

command = '''
if ! [ -x "$(command -v terraform)" ]; then
    cd $(mktemp --directory)
    cp /vagrant/terraform*.zip . --verbose
    sudo yum install zip unzip --assumeyes --verbose
    sudo unzip terraform*.zip -d /usr/bin
    rm terraform*.zip --verbose
fi
'''
subprocess.check_call(command, shell=True)
