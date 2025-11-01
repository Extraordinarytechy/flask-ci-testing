pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Extraordinarytechy/flask-ci-testing.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv ${VENV}
                . ${VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                pytest test_unit.py -v
                '''
            }
        }

        stage('Run Integration Tests') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                pytest test_integration.py -v
                '''
            }
        }

        stage('Run E2E Tests (Headless)') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                pytest test_e2e.py -v
                '''
            }
        }
    }

    post {
        always {
            junit '**/pytest.xml'
            echo 'All tests completed.'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
