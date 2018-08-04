# Cloudify CLI + Terraform

In this tutorial, Cloudify Manager will use Terraform to deploy an AWS VPC.

## create a directory as the working directory for Vagrant

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## download Terraform and unzip into the working directory

https://www.terraform.io/downloads.html

Linux https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip

## boot VM

According to `Vagrantfile`, Vagrant will:

* create a virtual machine of CentOS 7.2,
* install Cloudify CLI,
* install AWS CLI.

``` bash
vagrant up
```

## connect to VM

``` bash
vagrant ssh
```

## configure AWS CLI

Terraform will use [shared credentials](https://www.terraform.io/docs/providers/aws/) to authenticate AWS.

``` bash
aws configure
```

## deploy VPC

According to `example.yml`, Cloudify will call `install.sh` for `install`, which in turn calls `terraform apply`.

According to `example.tf`, Terraform will deploy an AWS VPC with an EC2 instance.

``` bash
cd /vagrant
cfy install example.yml --inputs "state=example" --blueprint-id "terraform-example" --verbose
```

## destroy VPC

According to `example.yml`, Cloudify will call `uninstall.sh` for `uninstall`, which in turn calls `terraform destroy`.

``` bash
cfy uninstall --blueprint-id "terraform-example" --verbose
```
