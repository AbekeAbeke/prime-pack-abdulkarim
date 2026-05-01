FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install .

ENTRYPOINT ["python", "-m", "prime_pack_abdulkarim"]