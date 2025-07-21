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
                // Start the Flask application
                sh 'export FLASK_APP=app.py'
                sh 'export FLASK_ENV=development'
                sh 'python app.py'
                // If using waitress for Windows:
                // sh 'waitress-serve --port=5000 app:app'
                // OR if you're just testing:
                //sh 'python -m flask run'
                
            }
        }
    }
}