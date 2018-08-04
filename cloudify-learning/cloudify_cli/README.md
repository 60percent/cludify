# A Quick Start Guide

In this tutorial, Cloudify CLI will be installed.

## download and install Vagrant

https://www.vagrantup.com/downloads.html

macOS https://releases.hashicorp.com/vagrant/2.0.2/vagrant_2.0.2_x86_64.dmg

## download and install VirtualBox

https://www.virtualbox.org/wiki/Downloads

macOS https://download.virtualbox.org/virtualbox/5.2.6/VirtualBox-5.2.6-120293-OSX.dmg

## add a box in Vagrant (China Mobile recommended)

``` bash
vagrant box add bento/centos-7.2
```

## get the list of installed boxes (including versions)

``` bash
vagrant box list
```

## create a directory as the working directory for Vagrant

## create a Vagrant file in the working directory

``` ruby
Vagrant.configure("2") do |config|

  config.vm.box = "bento/centos-7.2"
  config.vm.box_version = "2.3.1"
  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.network :forwarded_port, guest: 8000, host: 18000

  config.vm.provision "shell", inline: <<-SHELL
    sudo rpm --install /vagrant/cloudify-cli-community-*.rpm --verbose
  SHELL
end
```

## download Cloudify (Community) and copy into the working directory

https://cloudify.co/download/

Linux CLI http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-cli-community-18.2.1.rpm

Linux Manager http://repository.cloudifysource.org/cloudify/18.2.1/community-release/cloudify-manager-install-community-18.2.1.rpm

## boot VM

According to `Vagrantfile`, Vagrant will:

* create a virtual machine of CentOS 7.2,
* install Cloudify CLI.

``` bash
vagrant up
```

## connect to VM

``` bash
vagrant ssh
```

## play with Cloudify CLI

http://stage-docs.getcloudify.org/community-build/intro/evaluating-cloudify/

## destroy VM

``` bash
vagrant destroy
```
