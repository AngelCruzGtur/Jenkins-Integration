pipeline {
	agent any

	stages {
		stage('Build Java') {
			steps {
				bat 'mkdir build'
				bat 'javac -d build src\\HelloWorld.java'
			}
		}

		stage('Run Java') {
			steps {
				bat 'java -cp build HelloWorld'
			}
		}

		stage('Run Python Tests') {
			steps {
				bat 'run_tests.bat'
			}
		}
	}
}
