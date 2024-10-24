pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        } // stage Check scm
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        } // stage Build
        stage('Test') {
            agent { docker { image 'my-jenkins-image' }} // Використовуємо образ, де Tkinter встановлено
            steps {
                // Створюємо віртуальне середовище
                sh 'python3 -m venv venv'
                // Використовуємо pip з віртуального середовища
                sh 'venv/bin/pip install -r requirements.txt'
                sh 'venv/bin/python venv/bin/LAB4_programingTechnology_TEST.py'
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
        } // stage Test
    } // stages
} // pipeline
