pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        // stage('Setup') {
        //     steps {
        //         script {
        //             sh """
        //             pip install -r requirements.txt
        //             """
        //         }
        //     }
        // }
    }
    
}