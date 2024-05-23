FROM python:3.8-slim-buster

# RUN apt update -y && apt install awscii -y
# This command updates the package list (apt update -y) and 
# installs the AWS Command Line Interface (apt install awscli -y). The -y flag automatically answers "yes" to any prompts during the installation process.
WORKDIR /app
# This sets the working directory inside the Docker container to /app.
COPY . /app
# This command copies all the files from the current directory on the host machine (where the Dockerfile is located) to the /app directory in the Docker container.

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ['python3', 'streamlit_app.py']
# This sets the command to run when the container starts.
