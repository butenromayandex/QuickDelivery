pipeline {
    agent any
    environment {
        DOCKER_PWD = credentials('dockerpwd')
    }
    stages {
        stage('Install Docker') {
            agent {
                docker {
                    image 'docker:latest'
                }
            }
            steps {
                sh '''
                    docker -v
                    docker compose -v
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
                scripts {
                    @docker.image('docker:latest').inside {
                        sh 'docker-compose build'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                scripts {
                    @docker.image('docker:latest').inside {
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
    }

//     post {
//         always {
//             junit 'target/surefire-reports/*.xml'
//             archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
//         }
//     }
}