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
        stage('Install Helm') {
            steps {
                sh '''
                    curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
                    apt-get install apt-transport-https --yes
                    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
                    apt-get install helm
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
                docker {
                    image 'lachlanevenson/k8s-helm:v3.1.1'
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