# # FROM node

# # USER node
# # ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
# # ENV PATH=$PATH:/home/node/.npm-global/bin

# # WORKDIR /app/frontend
# # COPY package.json /app/frontend

# # COPY --chown=node:node package.json .
# # # RUN npm install
# # RUN npm i -g elm --unsafe-perm=true --allow-root
# # COPY --chown=node:node . .

# # RUN npm install


# FROM node
# RUN mkdir -p /app/frontend && chown -R node:node /app/frontend
# WORKDIR /app/frontend
# COPY package.json .
# USER node
# RUN npm install

# EXPOSE 3000
# CMD ["npm", "start"]

# # FROM node:lts
# # USER node
# # WORKDIR /home/node
# # COPY package.json .
# # RUN npm install
# # COPY . .
# # CMD ['npm', 'start']


FROM node:12.2.0-alpine

WORKDIR /app/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .

RUN npm install --silent

COPY src src

COPY public public

COPY .env .env

# RUN npm install react-scripts@3.0.1 -g --silent

EXPOSE 3000

CMD npm start