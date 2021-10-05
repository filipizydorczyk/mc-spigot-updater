#!/bin/python

from bs4 import BeautifulSoup
import requests
import os.path


SPIGOT_URL = "https://getbukkit.org/download/spigot"
env_ptah = os.getenv("MC_SERVER_JAR_PATH", "")

page = requests.get(SPIGOT_URL)
soup = BeautifulSoup(page.content, 'html.parser')

version = soup.find("div", {"id": "download"}).findAll(
    "div", {"class": "col-sm-3"})[0].h2.string

server_file = "spigot-{}.jar".format(version)
download_url = "https://download.getbukkit.org/spigot/{}".format(
    server_file)

path = os.path.join(env_ptah, server_file)

if(not os.path.isfile(path)):
    r = requests.get(download_url, allow_redirects=True)
    open(path, 'wb').write(r.content)
