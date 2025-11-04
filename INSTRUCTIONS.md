# Prereqs

first:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
py -m venv .samannotatortool     
.\.samannotatortool\Scripts\activate
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu118
