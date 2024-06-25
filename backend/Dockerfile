# 
FROM python:3.11 AS wattsup-base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM wattsup-base AS wattsup-dev


FROM wattsup-base AS wattsup-prod

COPY ./wattsup /code/wattsup

CMD ["fastapi", "run", "app/main.py", "--port", "80"]