# Cloudify CLI + Ansible

In this tutorial, we will use Cloudify Manager to install Ansible on vm created by Vagrant.

## create a directory ./rpm to store setup files 

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## boot VM

According to `Vagrantfile`, Vagrant will:

* create 3 virtual machine instances of CentOS 7.2,
* install Cloudify CLI, Manager on cfy instance.

``` bash
vagrant up
```

## connect to VM

``` bash
ssh vagrant@localhost -p <cfy instance mapping port>
cfy_manager install --private_ip 127.0.0.1 --public_id 192.168.0.11 -a admin
```


``` bash
cd /vagrant
cfy install ansible.yml --inputs "state=example" --blueprint-id "ansible-example" --verbose
```

## destroy VPC

According to `ansible.yml`, Cloudify will call `uninstall.sh` for `uninstall`, which in turn calls `Ansible destroy`.

``` bash
cfy uninstall --blueprint-id "ansible" --verbose
```
