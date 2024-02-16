import os

import requests
import zipfile

import env_local

env_local.loadEnvironmentVariables()
url = "https://api.github.com/repos/harshityadav95/Github-Actions/actions/artifacts/1248995138/zip"

payload = {}
headers = {
    'X-GitHub-Api-Version': '2022-11-28',
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer '+os.environ.get("SECRET_GITHUB_TOKEN")
}

response = requests.request("GET", url, headers=headers, data=payload)

filename = "artifact.zip"
if response.ok:
    with open(filename, "wb") as file:
        file.write(response.content)

os.mkdir("unzip_artifact")
current_dir = "./unzip_artifact"
with zipfile.ZipFile(filename, 'r') as zip_obj:
    zip_obj.extractall(current_dir)

print(response.text)
