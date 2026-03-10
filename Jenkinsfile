pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id') // Jenkins credentials ID
        IMAGE_BACKEND = "ankitrana/taskmanager-backend"
        IMAGE_FRONTEND = "ankitrana/taskmanager-frontend"
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/taskmanager-project.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_BACKEND ./backend'
                    sh 'docker build -t $IMAGE_FRONTEND ./frontend'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $IMAGE_BACKEND'
                    sh 'docker push $IMAGE_FRONTEND'
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                sh "docker-compose -f $COMPOSE_FILE up -d --build"
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Something went wrong!'
        }
    }
}
