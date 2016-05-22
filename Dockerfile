FROM python:3.5.1
MAINTAINER joway wong "joway.w@gmail.com"
RUN apt-get update && apt-get install -y mysql-client libmysqlclient-dev
RUN mkdir /i2pserver
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /i2pserver

WORKDIR /i2pserver
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]