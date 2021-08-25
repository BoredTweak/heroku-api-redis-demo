FROM tiangolo/uvicorn-gunicorn:python3.7

ARG REDIS_PORT 
ENV REDIS_PORT ${REDIS_PORT}
ARG REDIS_URL 
ENV REDIS_URL ${REDIS_URL}

COPY . /app
RUN pip install -U pip
RUN pip install -r /app/requirements.txt
