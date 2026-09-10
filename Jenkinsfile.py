pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git bramch:'main',url:'https://github.com/Ajay-23v/app.py.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirement.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'pytest test_app.py'
            }
        }
    }
}