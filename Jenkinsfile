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
                // Встановлення pip для поточного користувача
                sh 'python3 -m ensurepip --user || echo "pip already available"'
                sh 'python3 -m pip install --upgrade --user pip'
                
                // Встановлення залежностей для поточного користувача
                sh 'python3 -m pip install --user -r requirements.txt'
                
                // Створення директорії для звітів
                sh 'mkdir -p test-reports'
                
                // Запуск тестів
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
