pipeline {
    agent any

    environment {
        REPO = 'https://github.com/itsakrana/kubernetes_project.git'
        DOCKER_CREDENTIALS = 'dockerhub-creds'  // Jenkins Docker Hub credentials ID
        BACKEND_IMAGE = 'akrana2006/backend'  // Change to your Docker Hub repo
        FRONTEND_IMAGE = 'akrana2006/frontend' // Change to your Docker Hub repo
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: "${REPO}"  // Change branch if needed
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${BACKEND_IMAGE}:latest", "./backend")
                    docker.build("${FRONTEND_IMAGE}:latest", "./frontend")
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS}") {
                        docker.image("${BACKEND_IMAGE}:latest").push()
                        docker.image("${FRONTEND_IMAGE}:latest").push()
                        docker.image("${BACKEND_IMAGE}:latest").push('latest')
                        docker.image("${FRONTEND_IMAGE}:latest").push('latest')
                    }
                }
            }
        }

        stage('Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d --build'  // Make sure docker-compose.yml exists at repo root
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/'  // Applies all YAMLs in k8s folder
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
