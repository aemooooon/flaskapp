# A Python flask app Docker container which working with nginx proxy together for Virtualiztion Assginment 3

### Create a Flask Application Container
1. Make a directory 'flaskapp' to server as a build context for the Python/Flask application image. In that directory, create a dockerfile with the following contents:
```bash
FROM ubuntu:16.04
LABEL updated_on="2019-10-18 09:00"
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-setuptools python3-pip gunicorn3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

COPY lab-4-app /flaskapp
WORKDIR /flaskapp
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT "./startup.sh"
```
2. Clone the GitHub repository [aemooooon/lab-4-app]('https://github.com/aemooooon/lab-4-app') into your context.
3. Build container image with the tag: `docker build -t="aemooooon/flaskapp" .`
4. Run command `docker run -d --rm --name flaskapp -p 5000:5000 aemooooon/flaskapp` to test.
The application should works now, but for a production deployment we need to place it behind a reverse proxy server. For this, we will need a second container. Shut down flaskapp container.
