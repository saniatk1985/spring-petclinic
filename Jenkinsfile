#!groovy

pipeline {

    agent {
        label 'test1'
    }

    tools {
        maven "Maven 3.5.0"
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
        stage('Get Dependencies') {
            steps {
                echo 'Pre-Building Project...'
                sh "mvn -B dependency:resolve ${params.MAVEN_OPTS}"
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
                    echo 'deploying'
                },
                archive: {
                    archive 'target/*.jar'
                })
            }
        }
    }
}