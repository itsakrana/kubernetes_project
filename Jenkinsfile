pipeline {
agent any

```
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
            sh 'docker build -t akrana2006/backend:latest ./backend'
            sh 'docker build -t akrana2006/frontend:latest ./frontend'
        }
    }

    stage('Push Docker Images to DockerHub') {
        steps {
            withDockerRegistry([credentialsId: "${DOCKERHUB_CREDENTIALS}", url: 'https://index.docker.io/v1/']) {
                sh 'docker push akrana2006/backend:latest'
                sh 'docker push akrana2006/frontend:latest'
            }
        }
    }

    stage('Deploy to Kubernetes') {
        steps {
            sh 'kubectl apply -f k8s/'
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
```

}
