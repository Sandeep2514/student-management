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

	
	stage('Create Virtual Environment') {
     	    steps {
        	sh '''
        	python3 -m venv venv
        	. venv/bin/activate

        	pip install --upgrade pip

        	pip install -r student-service/requirements.txt
        	pip install -r course-service/requirements.txt
        	pip install -r result-service/requirements.txt
        	pip install -r api-gateway/requirements.txt
        	'''
    		}
	}
	stage('Validate Python Files') {
    	    steps {
        	sh '''
        	. venv/bin/activate

        	python -m py_compile student-service/app.py
        	python -m py_compile course-service/app.py
        	python -m py_compile result-service/app.py
        	python -m py_compile api-gateway/app.py
        	'''
   		 }
	}
	
	stage('SonarQube Analysis') {
    	    steps {
        	script {
            	      def scannerHome = tool 'SonarScanner'

           	      withSonarQubeEnv('SonarQube') {
                          sh """
                	  ${scannerHome}/bin/sonar-scanner \
                  	  -Dsonar.projectKey=Student-Management \
               		  -Dsonar.projectName=Student-Management \
                	  -Dsonar.sources=. \
                	  -Dsonar.sourceEncoding=UTF-8
                	  """
            	   }
        	 }
    	      }
	  }
   	
	stage('Quality Gate') {
 	   steps {
        	timeout(time: 5, unit: 'MINUTES') {
            	waitForQualityGate abortPipeline: true
       	   }
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
