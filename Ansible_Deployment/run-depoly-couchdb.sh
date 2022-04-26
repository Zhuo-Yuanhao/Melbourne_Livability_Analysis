#!/bin/bash

ansible-playbook -i hosts -u ubuntu --key-file=~/.ssh/CCC-T43-A2 deploy-couchdb.yaml