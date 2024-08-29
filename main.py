import sys
import os
from Operate_File.file_read import read_json
self_path = "/home/kanboyi/Codes/Data_Compresser"


cfg = read_json(os.path.join(self_path,'config.json'))
if __name__ == '__main__':
    print('Start_compressing')
    platform = sys.argv[1]
    taskname = sys.argv[2]

    directory = os.path.join(cfg['folder_path']['downloaded_path'],platform)
    output_filename = os.path.join(cfg['folder_path']['output_path'],f"{platform}-{taskname}.tar.gz")

    command = f'tar -czvf {output_filename} -C {directory} {taskname}'

    result = os.system(command)

    command_del = f'rm -r {directory}'
    result = os.system(command_del)