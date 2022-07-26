FROM gitpod/workspace-full

RUN pyenv update && pyenv install 3.10.5 && pyenv global 3.10.5
RUN pip install pipenv yapf

# remove PIP_USER environment
USER gitpod
RUN if ! grep -q "export PIP_USER=no" "$HOME/.bashrc"; then printf '%s\n' "export PIP_USER=no" >> "$HOME/.bashrc"; fi
