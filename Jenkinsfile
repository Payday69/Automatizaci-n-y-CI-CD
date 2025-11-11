pipeline {
    // Usamos el agente 'any' para que Jenkins ejecute esto en cualquier worker disponible.
    agent any

    // Definimos las etapas del proceso
    stages {
        stage('Preparacion') {
            steps {
                echo 'Iniciando la pipeline...'
                // Si tienes dependencias, aquí iría 'bat "pip install -r requirements.txt"'
            }
        }
        
        stage('Pruebas Unitarias') {
            steps {
                echo 'Ejecutando pruebas unitarias con unittest...'
                // 🛑 IMPORTANTE: Cambiamos 'sh' por 'bat'
                // Este comando ejecuta tus pruebas unitarias de Python.
                bat 'python test_math_utils.py && python test_string_utils.py'
            }
        }
        
        stage('Reporte') {
            steps {
                echo 'Verificando el resultado de las pruebas.'
            }
        }
    }
    
    // Acciones que se ejecutan después de que toda la pipeline termina
    post {
        always {
            echo 'Pipeline completada.'
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
