# Cloudify Manager + SSH (remote)

In this tutorial, Cloudify will use its Fabric (SSH) Plugin to deploy a python app on a remote host without Cloudify.

## create a directory as the working directory for Vagrant

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## download Cloudify Fabric Plugin and copy into the working directory

CentOS http://repository.cloudifysource.org/cloudify/wagons/cloudify-fabric-plugin/1.5.1/cloudify_fabric_plugin-1.5.1-py27-none-linux_x86_64-centos-Core.wgn

CentOS http://www.getcloudify.org/spec/fabric-plugin/1.5.1/plugin.yaml

## prepare the Python app

``` bash
COPYFILE_DISABLE=true tar czvf example.tar.gz example/
```

## boot VM

According to `Vagrantfile`, Vagrant will:

* create a virtual machine as `manager`,
* create a virtual machine as `client`,
* create a virtual machine as `node`.

``` bash
vagrant up
```

## connect to `manager`

``` bash
vagrant ssh manager
```

## install Cloudify Manager

``` bash
sudo cfy_manager install --private-ip 192.168.0.11 --public-ip 192.168.0.11 --admin-password "admin" --verbose
```

> The sanity test does not work correctly, but it seems safe to ignore.

## disconnect and connect to `client`

``` bash
exit
vagrant ssh client
```

## configure Cloudify CLI

``` bash
cfy profiles use 192.168.0.11 -u admin -p admin -t default_tenant
```

## verify Cloudify Manager

``` bash
cfy status
```

## install Cloudify Fabric Plugin

``` bash
cfy plugin upload -y /vagrant/cloudify_fabric_plugin-1.5.1-*.yaml /vagrant/cloudify_fabric_plugin-*.wgn --verbose
```

## upload Blueprint

``` bash
cfy blueprint upload -b python-example /vagrant/example.tar.gz --verbose
```

## install the Python app

``` bash
cfy deployment create -b python-example -i "ip=192.168.0.13" -i "user=vagrant" -i "password=vagrant" example --verbose
cfy executions start -d example install --verbose
```

## verify

``` bash
curl 192.168.0.13:5000
```

## uninstall the Python app

``` bash
cfy executions start -d example uninstall --verbose
```

## disconnect

``` bash
exit
```
