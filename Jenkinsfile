pipeline {

    agent any

    environment {
        PYTHON = "python3"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'git --version'
                sh 'python3 --version'
                sh 'java -version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install -r student-service/requirements.txt
                python3 -m pip install -r course-service/requirements.txt
                python3 -m pip install -r result-service/requirements.txt
                python3 -m pip install -r api-gateway/requirements.txt
                '''
            }
        }

        stage('Validate Python Files') {
            steps {
                sh '''
                python3 -m py_compile student-service/app.py
                python3 -m py_compile course-service/app.py
                python3 -m py_compile result-service/app.py
                python3 -m py_compile api-gateway/app.py
                '''
            }
        }

        stage('Verify Project Structure') {
            steps {
                sh 'find . -maxdepth 2 -type f'
            }
        }

    }

    post {

        success {
            echo "Build Successful"
        }

        failure {
            echo "Build Failed"
        }

        always {
            cleanWs()
        }

    }

}
