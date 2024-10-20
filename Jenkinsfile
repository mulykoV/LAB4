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
                bat 'python -m pip install --upgrade pip'
                bat 'pip install Flask xmlrunner'
                bat 'python app_tests.py'
                bat 'python --version'
                bat 'dir test-reports'

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
