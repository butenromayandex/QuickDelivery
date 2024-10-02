pipeline {
    agent any
    environment {
        DOCKER_PWD = credentials('dockerpwd')
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y docker docker-compose
                '''
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/butenromayandex/QuickDelivery.git'
            }
        }
        stage('Build') {
            steps {
                docker.image('docker:latest').inside {
                    sh 'docker-compose build'
                }
            }
        }
        stage('Deploy') {
            steps {
                docker.image('docker:latest').inside {
                    sh '''
                        docker image ls
                        docker login -u butenroma -p $DOCKER_PWD
                        docker push butenroma/logistics-service:latest
                        docker push butenroma/orders-service:latest
                    '''
                }
            }
        }
    }

//     post {
//         always {
//             junit 'target/surefire-reports/*.xml'
//             archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
//         }
//     }
}