## create a directory as the working directory for Vagrant

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## download Terraform and copy into the working directory

https://www.terraform.io/downloads.html

Linux https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip

## prepare Blueprint

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

## create Terraform Plugin

``` bash
wagon create -a '--no-cache-dir -c /vagrant/example/plugin/constraints.txt' --verbose /vagrant/example/plugin.zip
```

## install Terraform Plugin

``` bash
cfy plugin upload example_terraform_plugin*.wgn --verbose
```

## upload Blueprint

``` bash
cfy blueprint upload -b terraform-plugin-example /vagrant/example.tar.gz --verbose
```

## install Terraform

``` bash
cfy deployment create -b terraform-plugin-example -i "ip=192.168.0.13" -i "user=vagrant" -i "password=vagrant" terraform-plugin-example --verbose
cfy executions start -d terraform-plugin-example install --verbose
```

## disconnect and connect to `node`

``` bash
exit
vagrant ssh node
```

## verify

``` bash
terraform
```

## disconnect and connect to `client`

``` bash
exit
vagrant ssh client
```

## uninstall Terraform Plugin

``` bash
cfy plugin list
cfy plugin delete ...
rm *.wgn
```
