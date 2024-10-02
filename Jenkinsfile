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
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: '57f29692-c28f-409f-82ec-8bee5d39394b', variable: 'pwd')]) {
                    sh '''
                        docker login -u butenroma -p ${pwd}"
                        docker push butenroma/logistics-service
                        docker push butenroma/orders-service
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