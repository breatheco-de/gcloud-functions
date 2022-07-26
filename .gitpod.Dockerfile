FROM gitpod/workspace-postgres

RUN pyenv update && pyenv install 3.10.2 && pyenv global 3.10.2
RUN pip install pipenv yapf

# remove PIP_USER environment
USER gitpod
RUN if ! grep -q "export PIP_USER=no" "$HOME/.bashrc"; then printf '%s\n' "export PIP_USER=no" >> "$HOME/.bashrc"; fi
