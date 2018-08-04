from cloudify import ctx
from cloudify.decorators import operation

import subprocess

# https://docs.cloudify.co/4.2.0/plugins/creating-your-own-plugin/

@operation
def create(**kwargs):
    command = '''
    if ! [ -x "$(command -v terraform)" ]; then
        cd $(mktemp --directory)
        cp /vagrant/terraform*.zip . --verbose
        sudo yum install zip unzip --assumeyes --verbose
        sudo unzip terraform*.zip -d /usr/bin
        rm terraform*.zip --verbose
    fi
    '''
    ctx.logger.info('installing {0}'.format('Terraform'))
    subprocess.check_call(command, shell=True)
    ctx.logger.info('installed {0}'.format('Terraform'))

@operation
def delete(**kwargs):
    pass
