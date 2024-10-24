pipeline {
    agent { docker { image 'docker:dind' }}
    stages {
        stage('Build') {
            steps {
                script {
                    docker.image('lab4-jenkins:1.1').inside {
                        sh 'python3 -m venv venv'
                        sh 'venv/bin/pip install -r requirements.txt'
                        sh 'venv/bin/python venv/bin/LAB4_programingTechnology_TEST.py'
                    }
                }
            }
        }
    }
}
