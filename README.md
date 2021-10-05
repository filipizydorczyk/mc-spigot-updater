# 📥 Spigot updater

This python script scrapes the newsest uploaded spigot server from their [website](https://getbukkit.org/download/spigot) and download it if this version doesn't already exists. To let script knwo where spigot server is stored in filesystem define `MC_SERVER_JAR_PATH` env variable. If its not defined script will asume that you want to download file to directory that it was run in.

To install python dependencies type

```sh
make init
```

than you can run it with python

```sh
python ./main.py

# or you can copy it as sh script

cp ./main /some/path/update-spigot.sh
/some/path/spigot.sh
```
