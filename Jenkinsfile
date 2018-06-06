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
                
                sh "docker build -t saniatk1985/docker-project:${BUILD_NUMBER} ."
                
            }
        }
        stage('Docker push image') {
            steps {
               withDockerRegistry([ credentialsId: "dbce15cb-cb8c-468b-81ba-50c9cb39fa58", url: "" ]) {
          sh 'docker push saniatk1985/docker-project:${BUILD_NUMBER}'
          
                }
            }
        }

        stage('copy to remote host and start') {

             agent {
                docker {
                   image 'ansible/ansible'
                   args '--privileged --volume=/run/docker.sock:/var/run/docker.sock:rw'
               } 
           }

            steps {
                checkout scm
                withCredentials([[
                 $class: 'SSHUserPrivateKeyBinding',
                  credentialsId: '12334',
                  keyFileVariable: 'keyfile'
                  ]]) { 
                                
                sh 'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -vvv -i ./hosts --private-key=${keyfile} --extra-vars "build_number=${BUILD_NUMBER}" playbook_docker.yml'  
                //sh 'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${keyfile} --extra-vars "db_name=pc db_port=3306 db_user=san db_pass=1234 ap_user=san ap_pass=123456" playbook_app1.yml' 
             
}
                
            }
        }
        
    }
}
