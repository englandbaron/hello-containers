FROM python:3.6-slim

RUN mkdir /app

WORKDIR /app
RUN pip3 install --upgrade pip -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com
RUN pip install Django==2.2.1 -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com

ADD . .

EXPOSE 8080
ENTRYPOINT [ "python", "manage.py","runserver","0.0.0.0:8080" ]
