# hub.docker.comから公式で用意されたイメージをベースとする
FROM node:10.13-alpine

ENV APP_ROOT /app
WORKDIR $APP_ROOT

RUN npm install -g npm && \
    npm install -g yarn && \
    yarn global add vue-cli

COPY package.json $APP_ROOT
COPY yarn.lock $APP_ROOT

RUN yarn

ENV HOST 0.0.0.0

EXPOSE 8080
