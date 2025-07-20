pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/gopalvishwakarma/python-jenkins-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                // If using waitress for Windows:
                sh 'python app.py'
                // OR if you're just testing:
                // sh 'python -m flask run'
                
            }
        }
    }
}