FROM python:3-onbuild

COPY templates/style.css /usr/src/app/static/style.css
COPY templates/angular.js /usr/src/app/static/angular.js
COPY templates/js1.js /usr/src/app/static/js1.js


EXPOSE 5000

CMD ["python", "./app.py"]


