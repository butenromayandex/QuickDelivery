pipeline {
    agent any

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
                        docker-compose build
                    }
                }
            }
        }
//     stage('Test') {
//         steps {
//             script {
//                 docker.image('maven:3.6.3').inside {
//                     sh 'mvn test'
//                 }
//             }
//         }
//     }
    stage('Deploy') {
        steps {
            script {
                docker.image('docker:latest').inside {
                    sh 'docker push butenroma/logistics-service'
                    sh 'docker push butenroma/orders-service'
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