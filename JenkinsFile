pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'javac -d build src/HelloWorld.java'
            }
        }

        stage('Run') {
            steps {
                sh 'java -cp build HelloWorld'
            }
        }
    }
}
