FROM ubuntu:14.04
MAINTAINER Joway Wong "joway.w@gmail.com"
RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools supervisor git-core
RUN apt-get install python3-pip
RUN pip3 install virtualenv
RUN pip3 install uwsgi
RUN virtualenv --no-site-packages /opt/ve/djdocker
ADD . /opt/apps/djdocker
ADD .docker/supervisor.conf /opt/supervisor.conf
ADD .docker/run.sh /usr/local/bin/run
RUN /opt/ve/djdocker/bin/pip install -r /opt/apps/djdocker/requirements.txt
RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py migrate --noinput)
RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py collectstatic --noinput)
EXPOSE 8000
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
