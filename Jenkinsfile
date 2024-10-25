pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent { docker { image 'alpine'
                args '-u="root"' }
            }
            steps {
                // Встановлення Python і pip
                sh 'apk add --update python3 py3-pip'
                
                // Створення і активація віртуального середовища
                sh 'python3 -m venv /venv'
                sh '. /venv/bin/activate'
                
                // Встановлення пакетів з requirements.txt
                sh '/venv/bin/pip install -r /mnt/data/requirements.txt'
                
                // Запуск тестування
                sh '/venv/bin/python3 LAB4_programingTechnology_TEST.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
    }
}
