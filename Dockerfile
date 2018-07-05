FROM maven:latest as builder
WORKDIR /app
COPY . .
RUN mvn package -Dmaven.test.skip=true

FROM java:alpine
WORKDIR /app
RUN  addgroup -g 1000 -S user && \
    adduser -u 1000 -S user -G user
USER user
COPY --from=builder --chown=user:user /app/target/*.jar .
EXPOSE 8080
# ENTRYPOINT [ "/bin/sh" ]
CMD ["java","-jar","/app/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar"]
