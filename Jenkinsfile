pipeline {
    agent any
    environment {
        DOCKER_PWD = credentials('dockerpwd')
        HELM_RELEASE = "logistics-service"
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
                script {
                    docker.image('docker:latest').inside {
                        sh 'docker-compose'
                        sh 'docker-compose build'
                    }
                }
            }
        }
        stage('Push Docker Images') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    docker.image('docker:latest').inside {
                        sh '''
                            docker login -u butenroma -p $DOCKER_PWD
                            docker push butenroma/logistics-service:latest
                            docker push butenroma/order-service:latest
                        '''
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            agent {
                kubernetes {
                    containerTemplate {
                        name 'helm'
                        image 'lachlanevenson/k8s-helm:v3.1.1'
                        ttyEnabled true
                        command 'cat'
                    }
                }
            }
            steps {
                script {
                    sh "helm upgrade --install ${HELM_RELEASE} ./charts/logistics-service"
                }
            }
        }
    }
//     post {
//         always {
//             emailext (
//                 subject: "Build ${currentBuild.fullDisplayName}",
//                 body: "Check console output at ${env.BUILD_URL} to view the results.",
//                 recipientProviders: [[$class: 'DevelopersRecipientProvider']]
//             )
//         }
//     }
}