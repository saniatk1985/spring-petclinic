#!groovy

pipeline {

    agent {
        docker {
          image 'docker:latest'
        } 
    }

    

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                
                sh "docker build -t my_image:${BUILD_NUMBER} ."
                
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
