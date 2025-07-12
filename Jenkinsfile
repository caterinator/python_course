pipeline {
    agent any 
        /*{ 
        node {
            label 'docker-agent-python'
            }
      }*/
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ecbo "Built"
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "Tested"
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "Delivered"
                '''
            }
        }
    }
}
