FROM node: 16.15.0

WORKDIR /app
COPY ..
ENV PATH /app/node_modules/.bin:$PATH

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost, 127.0.0.1, localaddress, 172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au

COPY package*.json ./

RUN npm install
RUN npm install express

EXPOSE 8888
CMD["node", "app.js"]

