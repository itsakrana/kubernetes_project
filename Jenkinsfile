pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = 'github-cred'       // GitHub credential ID
        DOCKER_CREDENTIALS = 'dockerhub-cred' // Docker Hub credential ID
        DOCKER_IMAGE = 'itsakrana/taskmanager' // Docker image name
        COMPOSE_FILE = 'docker-compose.yml'    // Compose file
        K8S_MANIFEST = 'k8s/'                  // Folder containing k8s manifests
    }

    stages {

        stage('Checkout Code') {
            steps {
                git credentialsId: "${GIT_CREDENTIALS}", url: 'https://github.com/itsakrana/kubernetes_project.git', branch: 'master'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS}") {
                        // Backend
                        def backend = docker.build("${DOCKER_IMAGE}-backend", "./backend")
                        backend.push('latest')
                        
                        // Frontend
                        def frontend = docker.build("${DOCKER_IMAGE}-frontend", "./frontend")
                        frontend.push('latest')
                    }
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    sh "docker-compose -f ${COMPOSE_FILE} down -v"
                    sh "docker-compose -f ${COMPOSE_FILE} up -d --build"
                }
            }
        }

        stage('Kubernetes Deployment') {
            steps {
                script {
                    sh "kubectl apply -f ${K8S_MANIFEST}"
                }
            }
        }

    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
