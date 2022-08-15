import os
from pathlib import Path

from shutil import which, copyfile

__all__ = ['main']

api_path = os.getcwd()
env_path = Path(f'{api_path}/.env').resolve()
env_example_path = Path(f'{api_path}/.env.example').resolve()
where_in_docker = os.getenv('DOCKER') == '1'

copyfile(env_example_path, env_path)
