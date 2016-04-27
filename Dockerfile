FROM python:3-onbuild
VOLUME /blog
EXPOSE 8000

RUN pelican -s publishconf.py content

CMD ["make", "devserver"]
