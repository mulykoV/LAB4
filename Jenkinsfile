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
                sh 'apk add --update python3 py-pip'
                sh 'pip install -r requirements.txt'
                sh 'python3 LAB4_programingTechnology_TEST.py'
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
