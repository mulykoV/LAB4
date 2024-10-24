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
                // Перевіряємо наявність pip
                sh 'python3 -m pip --version || sudo apt-get install -y python3-pip'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
                
                // Створюємо директорію для звітів
                sh 'mkdir -p test-reports'
                
                // Запускаємо тести
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
