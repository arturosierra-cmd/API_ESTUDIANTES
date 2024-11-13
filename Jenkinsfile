pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git branch: 'main', credentialsId: 'tus_credenciales_id', url: 'https://github.com/usuario/tu_repositorio.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Instala las dependencias (modifica según tus necesidades)
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Ejecuta las pruebas (modifica según tu configuración de pruebas)
                sh 'pytest tests/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado con éxito.'
        }
        failure {
            echo 'Error en el pipeline.'
        }
    }
}
