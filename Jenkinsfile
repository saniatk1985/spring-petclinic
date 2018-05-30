#!groovy

pipeline {

    agent {
        dockerfile true 
    }

    tools {
        maven "Maven 3.5.3"
      }

    parameters {
        string(name: 'MAVEN_OPTS', defaultValue: '-Djava.awt.headless=true', description: 'Options for Maven')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Compiling Project...'
                sh "mvn -B dependency:resolve ${params.MAVEN_OPTS}"
                sh "mvn clean compile -B ${params.MAVEN_OPTS}"
            }
        }
        stage('Test and Package') {
            steps {
                echo 'Testing and Packaging Project..'
                sh "mvn package -B ${params.MAVEN_OPTS}"
            }
        }
        stage('Deploy') {
            steps {
                parallel(deploy: {
                    echo 'Deploying...'
                },
                archive: {
                    archive 'target/*.jar'
                })
            }
        }
    }
}
