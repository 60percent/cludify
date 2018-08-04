#!/bin/bash -e
cd ~/chef

knife bootstrap ${address} --ssh-user ${user} --ssh-password ${password} --sudo --use-sudo-password --node-name node1-ubuntu --run-list 'recipe[learn_chef_apache2]'

knife node list

knife node show node1-ubuntu

curl ${address}