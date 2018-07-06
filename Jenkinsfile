#!groovy

pipeline {

    agent none
    

    stages {
        
        stage('Checkout and Build') {
            agent
              {
             docker {
                image 'docker:latest'
                 args '--privileged --volume=/run/docker.sock:/var/run/docker.sock:rw'
                  } 
              }
            
            steps {
                checkout scm
                sh "docker build -t saniatk1985/docker-project:${BUILD_NUMBER} ."
                withDockerRegistry([ credentialsId: "dbce15cb-cb8c-468b-81ba-50c9cb39fa58", url: "" ]) {
                                   sh 'docker tag saniatk1985/docker-project:${BUILD_NUMBER} saniatk1985/docker-project:v1'
                                   sh 'docker push saniatk1985/docker-project:v1'
          
                                    }
                
            }
        }
        

        stage('copy to remote host and start') {

             agent any 

            steps {
                echo 'test'
                checkout scm
                withCredentials([[
                 $class: 'SSHUserPrivateKeyBinding',
                  credentialsId: '12334',
                  keyFileVariable: 'keyfile'
                  ]]) { 
                                
                sh 'su jenkins -c "kubectl apply -f app-deployment.yaml"'
             
                    }
                
            }
        }
        
    }
}
