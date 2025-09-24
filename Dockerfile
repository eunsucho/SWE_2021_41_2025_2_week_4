FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3

WORKDIR /app

CMD ["python3","/app/bind_mount/ishappy.py"]