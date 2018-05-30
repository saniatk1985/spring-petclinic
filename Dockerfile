FROM maven:latest as builder
WORKDIR /app
COPY . .
RUN mvn package

FROM java:alpine
WORKDIR /app

COPY --from=builder /app/target/*.jar .
COPY entry.sh .
ENTRYPOINT [ "/bin/sh" ]
CMD [ "entry.sh" ]