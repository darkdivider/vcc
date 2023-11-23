FROM python:3.9.17
WORKDIR /
COPY . /
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install Flask==2.0.1
RUN pip3 install jinja2==3.0.3
RUN pip3 install Werkzeug==2.2.2
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app6.py" ]