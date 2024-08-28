import os
import json

def build_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def write_txt(path,content):
    with open(path,"w",encoding = "utf-8") as file:
        file.write(content)

def dump_json(path,data):
    with open(path,"w",encoding = 'utf-8') as file:
        json.dump(data,file,indent = 4,ensure_ascii=False)