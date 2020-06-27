FROM python:3.8

# install and update required software
RUN apt-get update \
    && apt-get upgrade -y  --no-install-recommends \
    && apt-get install -y python3-psycopg2 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U pip

# copy project source code and install project dependencies
COPY . /src
RUN pip install -r /src/requirements.txt

# set container working directory
WORKDIR /src

EXPOSE 8000

# Run django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
