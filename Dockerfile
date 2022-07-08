FROM node:alpine
COPY package.json .
RUN yarn 
COPY . .
RUN yarn build
CMD [ "yarn", "start" ]