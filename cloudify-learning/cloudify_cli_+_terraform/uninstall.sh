#!/usr/bin/env bash
state="/vagrant/$1.tfstate"
./terraform destroy -state=$state -force
