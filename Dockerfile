# specify the image you want to use build docker image

FROM python:3.9.5

# Maintainer name to let people know who made this image.

MAINTAINER Akhil <akjain@deqode.com>


#apt is the ubuntu command line tool for advanced packaging tool(APT) for sw upgrade '''

#RUN apt update && \
 #   apt install -y netcat-openbsd

# set the env variable to tell where the app will be installed inside the docker

ENV INSTALL_PATH /Flask-Crud
RUN mkdir -p $INSTALL_PATH

#this sets the context of where commands will be ran in and is documented

WORKDIR $INSTALL_PATH

# Copy in the application code from your work station at the current directory
# over to the working directory.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .

RUN chmod +x /Flask-Crud/entrypoint.sh
CMD ["/bin/bash", "/Flask-Crud/entrypoint.sh"]