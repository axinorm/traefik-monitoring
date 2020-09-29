#!/usr/bin/python
import jinja2
import os

OS = os.getenv('TM_SERV_OS')
ARCH = os.getenv('TM_SERV_ARCH')
URL_TRAEFIK = os.getenv('TM_URL_TRAEFIK')
TEMPLATE_FILE = "docker-compose.yml.j2"

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(
  os=OS,
  arch=ARCH,
  url_traefik=URL_TRAEFIK
)

file = open("./docker-compose.yml", "w+")
file.write(outputText)
file.close()