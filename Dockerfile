FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /numismatics
WORKDIR /numismatics
ADD requirements.txt /numismatics/
RUN pip install -r requirements.txt
ADD . /numismatics/