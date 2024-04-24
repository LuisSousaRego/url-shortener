FROM python:3.12-bookworm
WORKDIR /app
RUN apt-get install libpq-dev
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./src /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

