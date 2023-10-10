FROM python:3.11.3

WORKDIR /TrackingDocker

COPY . /TrackingDocker/
RUN pip install --upgrade pip
RUN pip install -r /TrackingDocker/requirements.txt