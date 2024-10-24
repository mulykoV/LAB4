pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Перевірка версії Python
                    sh 'python3 --version || python --version'  // Показує версію Python
                    
                    // Забезпечити, що pip доступний
                    sh 'python3 -m ensurepip --upgrade || python -m ensurepip --upgrade'
                    
                    // Оновити pip
                    sh 'python3 -m pip install --upgrade pip || python -m pip install --upgrade pip'
                    
                    // Встановити залежності з requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Запустити тести
                    sh 'python3 LAB4_programingTechnology_TEST.py || python LAB4_programingTechnology_TEST.py'
                }
            }
            post {
                always {
                    // Перевірити наявність звітів про тести
                    sh 'ls -l test-reports'
                    // Зберегти результати тестування
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
