FROM python:3.9-alpine

COPY bots/findjobs.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "findjobs.py"]
