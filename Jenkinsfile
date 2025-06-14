pipeline {
    agent any

    environment {
        FLASK_PORT = "5012"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/Sastika2024/country-capital-app.git',
                    credentialsId: '53d0f794-adf5-4752-b7a7-6232bbdb7e5e',
			branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask App') {
            steps {
                bat 'start /B python app.py'
                sleep(time: 5, unit: 'SECONDS') // wait for server to start
            }
        }

        stage('Run Selenium Test') {
            steps {
                bat 'python tests\\test_app.py'
            }
        }
	environment {
        // Securely inject the Render deploy hook URL from Jenkins credentials
        RENDER_DEPLOY_HOOK = credentials('RENDER_DEPLOY_HOOK')
  	  }
        stage('Deploy to Render') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo '✅ All tests passed. Deploying to Render...'
                
                bat 'curl -X POST "%RENDER_DEPLOY_HOOK%"'
            }
        }
    }

    post {
        failure {
            echo '❌ Build or test failed.'
        }
    }
}
