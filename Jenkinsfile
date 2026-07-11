pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking Repository...'
            }
        }

        stage('Git Version') {
            steps {
                sh 'git --version'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Java Version') {
            steps {
                sh 'java -version'
            }
        }

        stage('Verify Services') {
            steps {
                sh 'ls -R'
            }
        }

    }

    post {

        always {

            echo 'Pipeline Completed'

        }

        success {

            echo 'Build Successful'

        }

        failure {

            echo 'Build Failed'

        }

    }

}
