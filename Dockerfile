FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV WORK_DIR=/work

RUN mkdir $WORK_DIR

WORKDIR $WEAPP_DIR

ADD requirements.txt $WORK_DIR/

RUN pip install -r requirements.txt

ADD . $WORK_DIR/
