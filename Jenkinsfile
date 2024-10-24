pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        } // stage Build
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        } // stage Build
        stage('Test') {
            agent { docker { image 'alpine'
                args '-u="root"' }
            }
            steps {
                sh 'apk add --update python3 py3-pip'
                sh 'python3 -m venv venv'
                // Використовуй python і pip з віртуального середовища
                sh 'venv/bin/pip install -r requirements.txt'
                sh 'venv/bin/python LAB4_programingTechnology_TEST.py'
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
}
