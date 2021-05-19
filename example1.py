#!/usr/bin/env python3
try:
    import requests
    import subprocess as cmd


    import os
except ImportError as exc:
    print(exc.msg)
    exit(1)
try:


    req = requests.get('https://pypi.org/pypi/ansible-core/json')
    print('Current ansible-core version is {}'.format(req.json()['info']['version']))
    value = input("Are you sure want to update? (Y/N) ")
    if value.lower() == "y":
        with open("result.txt", "w") as f:
            f.write('Current ansible-core version is {}'.format(req.json()['info']['version']))
        #cp = cmd.run("git clone https://github.com/nocman/Example01.git", check=True, shell=True)
        #cp = cmd.run("cd Example01/", check=True, shell=True)
        #cp = cmd.run("git init", check=True, shell=True)
        #cp = cmd.run("git pull origin main", check=True, shell=True)
        cp = cmd.run("git status", check=True, shell=True)
        cp = cmd.run("git add .", check=True, shell=True)
        cp = cmd.run(" git commit --allow-empty-message -m '' ", check=True, shell=True)
        if cp.returncode==0:
            print("no changes added to commit.")
        else:
            cp = cmd.run("git push -u origin main ", check=True, shell=True)
            print("thanks! result is updated successfully")
    elif value.lower() == "n":
        print("Bye")
        exit(1)
    else:
        print("Please choose the valid options")
except Exception as e:
    print("something went wrong:: " + str(e))
