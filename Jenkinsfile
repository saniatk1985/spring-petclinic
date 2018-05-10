#!groovy

pipeline {

    agent {
        label 'test1'
    }

    tools {
        maven "Maven 3.5.3"
      }

      
    environment {

    AWS_BIN = '/home/ec2-user/.local/bin/aws'

    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('build and test') {
            steps {
                echo 'Testing and Packaging Project..'
                sh "mvnw  package"
            }
        }
        stage('Deploy') {
            steps {
              withCredentials([[
                $class: 'AmazonWebServicesCredentialsBinding',
                credentialsId: '123',
                accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        ]]) {
              sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=eu-central-1 ${AWS_BIN} ec2 run-instances --image-id ami-778ba99c --count 1 --instance-type t2.micro --key-name san1 --security-group-ids sg-87ebb4ea --subnet-id subnet-87b4deca'
             // sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=eu-central-1 ${AWS_BIN} ec2 some-other-magic-commands' // this is aws cli ec2 command starting from last $

         }
                //parallel(deploy: {
                //    echo 'deploying'
                //},
                //archive: {
                //    archive 'target/*.jar'
                //})
            }
        }
    }
}
