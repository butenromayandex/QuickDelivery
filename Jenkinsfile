pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/butenromayandex/QuickDelivery.git'
            }
        }
//         stage('Build') {
//             steps {
//                 script {
//                     docker.image('maven:3.6.3').inside {
//                         sh 'mvn clean install'
//                     }
//                 }
//             }
//         }
//         stage('Test') {
//             steps {
//                 script {
//                     docker.image('maven:3.6.3').inside {
//                         sh 'mvn test'
//                     }
//                 }
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 script {
//                     docker.image('docker:latest').inside {
//                         sh 'docker-compose up -d'
//                     }
//                 }
//             }
//         }
    }

//     post {
//         always {
//             junit 'target/surefire-reports/*.xml'
//             archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
//         }
//     }
}