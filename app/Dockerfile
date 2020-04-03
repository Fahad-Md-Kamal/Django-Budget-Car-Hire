# pull official base image
# FROM python:3.8.0-alpine
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# RUN apk --no-cach add postgresql-dev \
#     gcc python3-dev musl-dev \
#     # wget dependency
#     openssl \
#     # dev dependencies
#     # git \
#     # bash \
#     # sudo \
#     # py3-pip \
#     # Pillow dependencies
#     jpeg-dev \
#     zlib-dev \
#     freetype-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tiff-dev \
#     tk-dev \
#     tcl-dev \
#     harfbuzz-dev \
#     fribidi-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# giving file permission locally
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]