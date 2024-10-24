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
               sh 'python3.11 -m ensurepip --upgrade'
                sh 'python3.11 -m pip install --upgrade pip'
                sh 'pip3.11 install -r requirements.txt'
                sh 'python3.11 app_tests.py'
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
