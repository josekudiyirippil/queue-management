FROM artifacts.developer.gov.bc.ca/docker-remote/node:22 as build-stage
ENV VUE_APP_PATH=/
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM artifacts.developer.gov.bc.ca/docker-remote/nginx:1.30.5 as production-stage
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir /app
COPY --from=build-stage /app/dist /app
EXPOSE 8080:8080
CMD ["nginx", "-g", "daemon off;"]