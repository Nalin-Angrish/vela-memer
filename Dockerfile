FROM node:slim
COPY package.json .
RUN yarn 
COPY . .
RUN yarn build
CMD [ "yarn", "start" ]