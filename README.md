# This Repo is a guide to create a fully automated CI/CD pipeline using GitHub Actions same can be done using Jenkins
## For startars there are 3 part of [workflow yml](./.github/workflows/main.yml) file :-
1. Docker 
2. terraform
3. ansible
## Roadmap

- the pipline utilize The [Dockerfile](./Dockerfile) to crate a docker image using a nginx:alpine image as base to setup web server image with [index.html](./index.html) as well as open port 80

- next the created custom imageis uploaded to my [dockhub](https://hub.docker.com/r/jagratsingh/nginx-html)

- after image is created next is provisioning of compute units for this we are using aws + [terraform](./terraform/main.tf) to get a load balancer and 3 web servers to run containers it also configure stuff like proxy network and image used as os

- the loadbalancer is address is out final link

- next is [ansible](./ansible/playbook.yml) + chef for orchestration and configuratinon 

- ansible installs docker and Chef .chef recipe file is created inside ansible itself 

- it image is downloaded and port 80 is opened which gives our web page at ip address of ec2 machine now load balancer distribute the users across the different ec2 machine reducing the load 

- the no of ec2 machine is a var in [terraform file](./terraform/main.tf) which can be changed as per trafic requirement 

- this currently deploy a simple webpage but same process can be sed for complex apps
