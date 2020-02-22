FROM python:3
COPY . /serialize
WORKDIR /serialize
RUN pip install -r req.txt
CMD python3 serialization.py