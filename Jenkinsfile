pipeline {
    agent any

    environment {
        FLASK_PORT = "5012"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: '53d0f794-adf5-4752-b7a7-6232bbdb7e5e', url: 'https://github.com/Sastika2024/country-capital-app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask App') {
            steps {
                sh 'nohup python app.py &'
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python test/test_ui.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
