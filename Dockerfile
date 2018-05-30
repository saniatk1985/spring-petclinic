FROM maven:latest as builder
WORKDIR /app
COPY . .
RUN mvn package

FROM java:alpine
WORKDIR /app
RUN useradd user
USER user
COPY --from=builder --chown=user /app/target/*.jar .
ENV DB_USER=myuser
ENV DB_HOST=mysql
ENV DB_PASS=1234
ENTRYPOINT [ "/bin/sh" ]
CMD ["java","-jar","/app/*.jar"]
