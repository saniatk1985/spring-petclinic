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
                                   sh 'docker push saniatk1985/docker-project:${BUILD_NUMBER}'
          
                                    }
                
            }
        }
        

        stage('copy to remote host and start') {

             agent any //{
                //docker {
                  // image 'williamyeh/ansible:ubuntu16.04'
                   //args '--privileged --volume=/run/docker.sock:/var/run/docker.sock:rw'
               //} 
           //}

            steps {
                echo 'test'
                checkout scm
                withCredentials([[
                 $class: 'SSHUserPrivateKeyBinding',
                  credentialsId: '12334',
                  keyFileVariable: 'keyfile'
                  ]]) { 
                                
                sh 'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${keyfile} --user ec2-user --extra-vars "build_number=${BUILD_NUMBER}" playbook_docker.yml'  
                //sh 'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${keyfile} --extra-vars "db_name=pc db_port=3306 db_user=san db_pass=1234 ap_user=san ap_pass=123456" playbook_app1.yml' 
             
                    }
                
            }
        }
        
    }
}
