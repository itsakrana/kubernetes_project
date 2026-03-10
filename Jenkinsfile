pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git credentialsId: 'github-cred',
                url: 'https://github.com/itsakrana/kubernetes_project.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t akrana2006/backend:latest ./backend'
                sh 'docker build -t akrana2006/frontend:latest ./frontend'
            }
        }

        stage('Push Docker Images') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-cred', url: '']) {
                    sh 'docker push akrana2006/backend:latest'
                    sh 'docker push akrana2006/frontend:latest'
                }
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                sh 'docker rm -f taskmanager-db taskmanager-backend || true'
            }
        }

        stage('Docker Compose') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
