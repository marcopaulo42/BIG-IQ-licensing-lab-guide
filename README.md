# VE Licensing with BIG-IQ Lab Documentation

This repository contains documentation for the VE Licensing with BIG-IQ Lab. The main documentation is built using
[Sphinx](https://www.sphinx-doc.org/en/master/index.html) and is meant to be packaged into an NGINX container
and served from the UDF environment.

## Setup

Install Sphinx using any supported method. A `requirements.txt` file is provided in this repository for installing
Sphinx and this repository's dependencies into a virtual environment.

 - F5 Sphinx theme can be found here: `https://github.com/f5devcentral/f5-sphinx-theme/releases`
 - Sphinx documentation can be found here: `https://www.sphinx-doc.org/en/master/index.html`
 - Python virtual environment documentation can be found here: `https://python.land/virtual-environments/virtualenv`
 - CloudDocs home page can be found here `https://docs.f5net.com/pages/viewpage.action?spaceKey=F5CLDDOCS&title=CloudDocs+Home`

If using BIG-IP VE Licensing with BIG-IQ
 - connect to Ubuntu jump host
   > **_Note:_** requires UDF SSH Key setup via `UDF-> Preferences`
   ```bash
   ssh <udf uuid>.access.udf.f5.com -p 47002
   ```
 - download this repo
   ```bash
   wget https://github.com/marcopaulo42/BIG-IQ-licensing-lab-guide/archive/refs/tags/<current version>.tar.gz
   ```
 - unzip file
   ```bash
   tar xzf <current version>.tar.gz
   ```
 - change to unzipped directory
   ```bash
   cd BIG-IQ-licensing-lab-guide-<current version>
   ```   
 - enter python virtual environment (requires `python3-venv` and `python3`)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   cd docs
   make html
   deactivate
   ```
 - copy newly created files to home directory
   ```bash
   cp -r ./docs/_build/html/ ~
   ```
  
 - stop previous docker container running NGINX webserver hosting documents
   ```bash
   sudo docker ps -a
   sudo docker stop <container name>
   sudo docker rm <container name>
   ```
 - start new docker container running NGINX webserver and map to new html directory
   ```bash
   sudo docker run --name docker-nginx -p 8080:80 -d --restart unless-stopped -v /home/ubuntu/html:/usr/share/nginx/html nginx
   ```

## summary.md

The [summary.md](summary.md) file should be copied into the Documentation tab in UDF.

## Initial Setup of Ubuntu Jump host in UDF
The following commands are used to setup the Ubuntu Jumphost hosted in UDF. The setup allows a docker container to run at startup, and hosts an NGINX webserver which presents the above lab guide.

```bash
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo systemctl enable --now docker
sudo apt install python3-venv
sudo apt install make
sudo docker pull nginx
```
Perform the commands above to download the BIG-IQ lab guide, make it, and move it to the ~/html directory, and then run the following command to run the NGINX docker image:
```bash
sudo docker run --name docker-nginx -p 8080:80 -d --restart unless-stopped -v /home/ubuntu/html:/usr/share/nginx/html nginx
```

## Maintainer

* Marco dos Santos
* and originally created by Paul Teiber - <p.teiber@f5.com>
