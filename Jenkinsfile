pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
            }
        }
        stage('Test') {
            steps {
                // Використовувати Python 3.11.9
                sh 'python3 -m ensurepip --upgrade'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 LAB4_programingTechnology_TEST.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Tests passed successfully!"
                }
                failure {
                    echo "Tests failed!"
                }
            }
        }
    }
}
