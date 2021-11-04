FROM python:3.7-alpine

WORKDIR .
# RUN mkdir /backend
# WORKDIR /backend

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]