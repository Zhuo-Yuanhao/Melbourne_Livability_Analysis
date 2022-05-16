# Ansible Deployment
## Prerequisites
1. Need to login to MRC Dashboard and download the openrc.sh 
<img width="1121" alt="image" src="https://user-images.githubusercontent.com/81127118/168543808-de391c89-c4fb-4e7d-b7c0-e5ca370d2be5.png">
2. Reset API password
<img width="908" alt="image" src="https://user-images.githubusercontent.com/81127118/168543936-47bb07c8-74af-44a5-ac50-68505e495721.png">
3.	Get information to set instance:

–	availability_zone: melbourne-qh2-uom

–	instance_image: 356ff1ed-5960-4ac2-96a1-0c0198e6a999

–	instance_key_name: CCC-T43-A2 

–	instance_flavor: uom.mse.2c9g


## User Guide
1. Connect to VPN(Cisoco)
2. For create instances on MRC: RUN ‘run-nectar.sh’
3. For deploy cluster CouchDB on instance: RUN ‘run-depoly-couchdb.sh’
4. For clone GitHub codes to instance: RUN ‘run-clone-git.sh’
5. For deploy tweet crawler and data pre-processing codes on instance: RUN ‘run-tweet-crawler.sh’
6. For deploy front-end codes on instance: RUN ‘run-frontend.sh’
