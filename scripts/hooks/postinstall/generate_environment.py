import os
from pathlib import Path

from shutil import which, copyfile

__all__ = ['main']

api_path = os.getcwd()
env_path = Path(f'{api_path}/.env').resolve()
env_example_path = Path(f'{api_path}/.env.example').resolve()
where_in_docker = os.getenv('DOCKER') == '1'

if which('gp'):
    copyfile(env_example_path, env_path)
    exit()

content = ''
with open(env_example_path, 'r') as file:
    lines = file.read().split('\n')

# for line in lines:
#     try:
#         key, value = line.split('=')

#     except:
#         content += '\n'

with open(env_path, 'w') as file:
    file.write(content)
