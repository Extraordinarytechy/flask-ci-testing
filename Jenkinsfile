pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Extraordinarytechy/flask-ci-testing.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '. venv/bin/activate && pytest test_unit.py -v --junitxml=results_unit.xml'
            }
        }

        stage('Run Integration Tests') {
            steps {
                sh '. venv/bin/activate && pytest test_integration.py -v --junitxml=results_integration.xml'
            }
        }

        stage('Run E2E Tests (Headless)') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python app.py &
                sleep 5
                pytest test_e2e.py -v --junitxml=results_e2e.xml
                '''
            }
        }

        stage('Code Quality Scan (SonarQube)') {
            environment {
                SONAR_SCANNER_HOME = tool 'SonarScanner'
            }
            steps {
                withSonarQubeEnv('SonarLocal') {
                    sh '''
                    $SONAR_SCANNER_HOME/bin/sonar-scanner \
                      -Dsonar.projectKey=flask-ci-testing \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000
                    '''
                }
            }
        }
    }

    post {
        always {
            junit '**/results_*.xml'
        }
        success {
            echo 'All tests and SonarQube scan completed successfully.'
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
    }
}
