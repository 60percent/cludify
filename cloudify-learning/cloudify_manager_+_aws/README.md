# Cloudify Manager + AWS

In this tutorial, Cloudify will use its AWS plugin to deploy an AWS VPC.

## create a directory as the working directory for Vagrant

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## download Cloudify AWS Plugin and copy into the working directory

CentOS https://github.com/cloudify-cosmo/cloudify-aws-plugin/releases/download/1.5.1.2/cloudify_aws_plugin-1.5.1.2-py27-none-linux_x86_64-centos-Core.wgn

CentOS 
https://github.com/cloudify-cosmo/cloudify-aws-plugin/releases/download/1.5.1.2/plugin.yaml

## boot VM

According to `Vagrantfile`, Vagrant will:

* create a virtual machine of CentOS 7.2,
* install Cloudify Manager.

> The sanity test does not work correctly, but it seems safe to ignore.

``` bash
vagrant up
```

## view Cloudify Manager

> http://localhost:2280/

## connect to VM

``` bash
vagrant ssh
```

## configure Cloudify CLI

``` bash
cfy profiles use 127.0.0.1 -u admin -p admin -t default_tenant
```

## verify Cloudify Manager

``` bash
cfy status
```

## install Cloudify AWS Plugin

``` bash
cfy plugin upload -y /vagrant/cloudify_aws_plugin-*.yaml /vagrant/cloudify_aws_plugin-*.wgn --verbose
```

## configure Cloudify AWS Plugin

``` bash
cfy secrets create aws_access_key_id -s ...
cfy secrets create aws_access_key_value -s ...
```

## upload Blueprint

``` bash
cd /vagrant
cfy blueprint upload -b aws-example example.yaml --verbose
```

## deploy VPC

According to `example.yml`, Cloudify will deploy an AWS VPC with an EC2 instance.

``` bash
cfy deployment create -b aws-example example --verbose
cfy executions start -d example install --verbose
```

> A subscription in `aws marketplace` is required for the first time.

## destroy VPC

``` bash
cfy executions start -d example uninstall --verbose
```

> The `Volumn` deletion may not work correctly.
