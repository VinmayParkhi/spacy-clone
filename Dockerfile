FROM  python:3.10

ENV DEBIAN_FRONTEND interactive
ENV TERM linux

ENV DEBIAN_FRONTEND teletype
ENV PYTHONIOENCODING "utf-8"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext-base \
    libsm6 \
    libxext6 \
    libxrender-dev\
    libffi-dev \
    libldap2-dev \
    libpq-dev \
    libsasl2-dev \
    nginx-light \
    supervisor \
    wget && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-pil \
    python3-requests \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD . /app/
RUN pip3 install spacy
RUN python -m spacy download en_core_web_sm
#RUN python -m spacy download en_core_web_lg
RUN python -m spacy link en_core_web_lg en
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
