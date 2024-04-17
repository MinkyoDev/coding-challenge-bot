FROM python:3.10-alpine

WORKDIR /workspace

COPY . /workspace

RUN pip install -r requirements.txt

CMD ["python", "main.py"]