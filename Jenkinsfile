pipeline {
	agent any

	stages {
		stage('Build Java') {
			steps {
				bat '''
				if not exist build (
					mkdir build
				)
				javac -d build src\\HelloWorld.java
				'''
			}
		}

		stage('Run Java') {
			steps {
				bat 'java -cp build HelloWorld'
			}
		}
	}
}
