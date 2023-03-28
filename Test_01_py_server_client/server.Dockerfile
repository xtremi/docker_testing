FROM python:3.12.0a6-alpine3.17
WORKDIR /.

COPY ./python_server/server.py .

EXPOSE 3000
CMD ["python", "server.py"]
