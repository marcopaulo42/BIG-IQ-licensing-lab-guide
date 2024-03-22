# VE Licensing with BIG-IQ Lab Documentation

This repository contains documentation for the VE Licensing with BIG-IQ Lab. The main documentation is built using
[Sphinx](https://www.sphinx-doc.org/en/master/index.html) and is meant to be packaged into an NGINX container
and served from the UDF environment.

## Setup

Install Sphinx using any supported method. A requirements.txt file is provided in this repository for installing
Sphinx and this repository's dependencies into a virtual environment.

If using BIG-IP VE Licensing with BIG-IQ
 - connect to Ubuntu jump host
   `ssh <udf uuid>.access.udf.f5.com -p 47002`
 - download this repo
   `wget https://github.com/marcopaulo42/BIG-IQ-licensing-lab-guide/archive/refs/tags/<current version>.tar.gz`
 - unzip file
   `tar xzf <current version>.tar.gz`
 - enter python virtual environment (requires python3-venv and python3)
   `python -m venv .venv`
   `source .venv/bin/activate`
   `pip install -r requirements.txt`
   `cd docs/`
  ` make html`
   `deactivate`
 - stop previous docker container running NGINX webserver hosting documents
   `sudo docker ps -a`
   `sudo docker stop <container name>`
 - start new docker container running NGINX webserver and map to new html directory
   `sudo docker run --name docker-nginx -p 8080:80 -d -v /home/ubuntu/<BIG-IQ-licensing-lab-guide path>/docs/_build/html:/usr/share/nginx/html nginx`

## summary.md

The [summary.md](summary.md) file should be copied into the Documentation tab in UDF.

## Maintainer

* Marco dos Santos
* and originally created by Paul Teiber - <p.teiber@f5.com>
