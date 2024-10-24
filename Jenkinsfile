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
            steps {
               agent {
                    docker {
                            image 'lab4-jenkins:1.1'
                            args '-u root:root' // додає можливість запускати з правами root
                            }
                    }
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
