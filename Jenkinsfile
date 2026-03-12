pipeline {
agent any

environment {
    DOCKERHUB_CREDENTIALS = 'dockerhub-cred'
    GITHUB_CREDENTIALS = 'github-cred'
}

stages {

    stage('Checkout Code') {
        steps {
            git credentialsId: "${GITHUB_CREDENTIALS}",
                url: 'https://github.com/itsakrana/kubernetes_project.git'
        }
    }

    stage('Build Docker Images') {
        steps {
            sh 'docker build -t backend-image:latest ./backend'
            sh 'docker build -t frontend-image:latest ./frontend'
        }
    }

    stage('Tag Images for DockerHub') {
        steps {
            sh 'docker tag backend-image:latest akrana2006/backend-image:latest'
            sh 'docker tag frontend-image:latest akrana2006/frontend-image:latest'
        }
    }

    stage('Push Docker Images to DockerHub') {
        steps {
            withDockerRegistry([credentialsId: "${DOCKERHUB_CREDENTIALS}", url: 'https://index.docker.io/v1/']) {
                sh 'docker push akrana2006/backend-image:latest'
                sh 'docker push akrana2006/frontend-image:latest'
            }
        }
    }

    stage('Deploy to Kubernetes') {
        steps {
            sh 'kubectl apply -f k8s/ --validate=false'
        }
    }

    stage('Verify Deployment') {
        steps {
            sh 'kubectl get all -n taskmanager'
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

