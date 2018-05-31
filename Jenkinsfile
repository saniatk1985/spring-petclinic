#!groovy

pipeline {

    agent {
        docker {
          image 'docker:latest'
          args '--privileged --volume=/run/docker.sock:/var/run/docker.sock:rw'
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
                
                sh "docker build -t docker-project:${BUILD_NUMBER} ."
                
            }
        }
        stage('Docker push image') {
            steps {
               withDockerRegistry([ credentialsId: "dbce15cb-cb8c-468b-81ba-50c9cb39fa58", url: "" ]) {
          sh 'docker push saniatk1985/docker-project:${BUILD_NUMBER}'
          
                }
            }
        }
        
    }
}
