FROM python:3.7-alpine

WORKDIR .

# RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5006

COPY . .
CMD ["python3 -m", "grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto"]
CMD ["python3", "main.py"]