FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /numismatics
WORKDIR /numismatics
ADD requirements.txt /numismatics/
RUN pip install -r requirements.txt
ADD . /numismatics/