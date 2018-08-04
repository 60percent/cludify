#!/usr/bin/env bash
state="/vagrant/$1.tfstate"
./terraform init
./terraform apply -state=$state -auto-approve
