pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio en la rama especificada
                git branch: 'main', credentialsId: '6d3cceec-016a-4d32-9bfa-1445ab91b1b6', url: 'https://github.com/arturosierra-cmd/API_ESTUDIANTES.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Elimina el entorno virtual si existe y crea uno nuevo, luego instala dependencias
                sh 'rm -rf venv'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Code Analysis') {
            steps {
                // Verifica la ubicación de pylint y luego ejecuta el análisis de código
                sh '. venv/bin/activate && which pylint'
                sh '. venv/bin/activate && pylint test/test_app.py'
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecuta las pruebas
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('Push to GitHub') {
            when {
                branch 'main'
            }
            steps {
                // Si todas las etapas anteriores pasan, realiza un push al repositorio
                withCredentials([usernamePassword(credentialsId: '6d3cceec-016a-4d32-9bfa-1445ab91b1b6', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    sh """
                        git config --global user.email "g.arturosierra@outlook.com"
                        git config --global user.name "arturosierra-cmd"
                        git add .
                        git commit -m "Auto commit after successful build"
                        git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/arturosierra-cmd/API_ESTUDIANTES.git HEAD:main
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Validación completada y cambios subidos a GitHub.'
        }
        failure {
            echo 'Falló la validación. No se subieron cambios.'
        }
    }
}
