#!/bin/bash -e
sudo apt-get update
sudo apt-get -y install curl git
curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P chefdk -c stable -v 2.0.28

mkdir ~/chef
cd ~/chef
mkdir .chef
cd .chef
cp /drop/chefadmin.pem chefadmin.pem

cat <<EOT >> knife.rb
current_dir = File.dirname(__FILE__)
log_level                 :info
log_location              STDOUT
node_name                 "chefadmin"
client_key                "#{current_dir}/chefadmin.pem"
chef_server_url           "https://chef_server/organizations/4thcoffee"
cookbook_path             ["#{current_dir}/../cookbooks"]
EOT

cd ~/chef
knife ssl fetch
mkdir cookbooks
cd cookbooks
git clone https://github.com/learn-chef/learn_chef_apache2.git
knife cookbook upload learn_chef_apache2

