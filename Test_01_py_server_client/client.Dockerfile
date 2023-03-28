FROM python:3.12.0a6-alpine3.17
WORKDIR /.

RUN pip install httplib2

COPY ./python_client/client.py .

EXPOSE 3000
CMD ["python", "client.py"]
