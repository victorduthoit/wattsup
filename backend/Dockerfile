# 
FROM python:3.11 AS base

WORKDIR /opt/code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt update -y
#RUN apt install sudo vim nano htop
CMD ["bash"]

FROM base AS dev

#RUN apt install git
CMD ["sleep", "infinity"]

FROM base AS prod

COPY ./wattsup /optcode/wattsup


CMD ["fastapi", "run", "app/main.py", "--port", "80"]