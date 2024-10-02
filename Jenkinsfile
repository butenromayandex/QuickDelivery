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
                sh '''
                    docker-compose build
                '''
                }
            }
        }
         stage('Deploy') {
                steps {
                    script {
                        sh 'docker push butenroma/logistics-service'
                        sh 'docker push butenroma/orders-service'
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

//     post {
//         always {
//             junit 'target/surefire-reports/*.xml'
//             archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
//         }
//     }
}