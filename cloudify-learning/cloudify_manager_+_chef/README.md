# Cloudify Manager + AWS

In this tutorial, Cloudify will install agent on provised host and start a SimpleHTTPServer using this agent.

## create a directory as the working directory for Vagrant

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm


## boot VM

According to `Vagrantfile`, Vagrant will:

* create a virtual machine hosting Cloudify Manager
* create a virtual machine to start SimpleHTTPServer

> The sanity test does not work correctly, but it seems safe to ignore.

``` bash
vagrant up
```

## view Cloudify Manager

> http://localhost:2280/

## connect to VM

``` bash
vagrant ssh manager
```

## install Cloudify Manager

``` bash
cfy_manager install --private-ip 192.168.33.17 --public-ip 192.168.33.17 --admin-password "admin" --verbose
```

## configure Cloudify CLI

``` bash
cfy profiles use 192.168.33.17 -u admin -p admin -t default_tenant
```

## verify Cloudify Manager

``` bash
cfy status
```

## upload Blueprint

``` bash
cd /vagrant/src
cfy blueprint upload -b example  blueprint.yaml --verbose
```

## install agent on host and start SimpleHTTPServer

According to `blueprint.yml`, Cloudify will install agent on the host then install chef server and chef dk on the host. Then we use chef to deploy a apache server on another host.
Notice that, the host machine will get agent installation file from Cloudify Manger by its private IP.
Therefore, when installing Cloudify Manger, we need to specify its private ip which must be accessible to all machines for deployment.

``` bash
cfy deployment create -b example example -i '{"chef_server_ip": "192.168.33.18", "chef_agent_ip": "192.168.33.19"}' --verbose
cfy executions start -d example install --verbose
```

## destroy VPC

``` bash
cfy executions start -d example uninstall --verbose
```
