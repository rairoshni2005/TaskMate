pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install selenium webdriver-manager'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python3 selenium-tests/test_add_task.py'
                sh 'python3 selenium-tests/test_delete_task.py'
                sh 'python3 selenium-tests/test_complete_task.py'
                sh 'python3 selenium-tests/test_load_tasks.py'
                sh 'python3 selenium-tests/test_filter_tasks.py'
                sh 'python3 selenium-tests/test_theme_toggle.py'
            }
        }
    }
}