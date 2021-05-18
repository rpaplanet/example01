#!/usr/bin/env python3
try:
  import requests
  import os
except ImportError as exc:
  print(exc.msg)
  exit(1)
try:
  script_path = os.path.abspath(__file__)
  folder_path = os.path.split(script_path)
  project_folder = folder_path[0]
  print(project_folder)
  path=project_folder+"/result/result.txt"
  req = requests.get('https://pypi.org/pypi/ansible-core/json')
  print('Current ansible-core version is {}'.format(req.json()['info']['version']))
  value = input("Are you sure want to update? (Y/N) ")
  if value.lower() =="y":
    with open(path,"w") as f:
      f.write('Current ansible-core version is {}'.format(req.json()['info']['version']))
    print("thanks! result is updated")
  elif value.lower() =="n":
    print("Bye")
    exit(1)
  else:
    print("Please choose the valid options")
except Exception as e:
  print("something went wrong:: " + str(e))
