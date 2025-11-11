pipeline {
    // Usamos el agente 'any' para que Jenkins ejecute esto en cualquier worker disponible.
    agent any

    // Definimos las etapas del proceso
    stages {
        stage('Preparacion') {
            steps {
                echo 'Iniciando la pipeline...'
                // Opcional: Crear un entorno virtual si usas dependencias
                // sh 'python -m venv venv'
                // sh '. venv/bin/activate' 
                // sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Pruebas Unitarias') {
            steps {
                echo 'Ejecutando pruebas unitarias con unittest...'
                // Ejecuta todos los archivos de prueba que comienzan con 'test_'
                // El comando -m unittest discover busca y ejecuta tus pruebas.
                sh 'python -m unittest discover' 
            }
        }
        
        stage('Reporte') {
            steps {
                echo 'Verificando el resultado de las pruebas.'
                // Opcional: Podrías añadir lógica aquí para notificar 
                // si las pruebas fallaron o para generar un reporte visual.
            }
        }
    }
    
    // Acciones que se ejecutan después de que toda la pipeline termina
    post {
        always {
            echo 'Pipeline completada.'
            // Esto es útil si quieres saber el resultado final de la ejecución
            script {
                if (currentBuild.result == 'SUCCESS') {
                    echo '¡Construcción exitosa!'
                } else {
                    echo '¡Construcción fallida!'
                }
            }
        }
    }
}
