pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'mkdir build'
                bat 'javac -d build src\\HelloWorld.java'
            }
        }

        stage('Run') {
            steps {
                bat 'java -cp build HelloWorld'
            }
        }
    }
}
