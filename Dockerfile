FROM python:3.9.2-slim-buster

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","run.sh"]
