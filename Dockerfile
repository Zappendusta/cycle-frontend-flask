FROM ubuntu
RUN apt-get update  --security-opt seccomp:unconfined 
RUN apt-get install -y python python-pip python-dev

COPY ./pip_requirements.txt /app/pip_requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "cycle.py" ]

