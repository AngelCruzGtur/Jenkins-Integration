pipeline {
	agent any

	stages {
		stage('Build Java') {
			steps {
				sh 'mkdir -p build'
				sh 'javac -d build src/HelloWorld.java'
			}
		}

		stage('Run Java') {
			steps {
				sh 'java -cp build HelloWorld'
			}
		}

		stage('Run Shell Script') {
			steps {
				sh './Hello_world.sh'
			}
		}
	}
}
