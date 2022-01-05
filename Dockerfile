#FROM ubuntu
#RUN apt-get update
#RUN apt-get install -y python3 python3-pip

FROM python
COPY ./pip_requirements.txt /app/pip_requirements.txt

WORKDIR /app

RUN pip install -r pip_requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "cycle.py" ]

