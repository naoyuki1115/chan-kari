FROM node:14.17.5

ENV LANG=C.UTF-8
ENV TZ=Asia/Tokyo
RUN npm install -g npm
RUN npm install react-router-dom
RUN npm i --save @fortawesome/fontawesome-svg-core
RUN npm install --save @fortawesome/free-solid-svg-icons
RUN npm install --save @fortawesome/react-fontawesome

#RUN npm audit fix
RUN npm install react-bootstrap bootstrap

WORKDIR /usr/src/app/frontend/
#WORKDIR /usr/src/app/
