pipeline {
	agent any
	stages {
		stage("build") {
			steps {	
				sh 'docker build -t david:${BUILD_NUMBER} .'
			}
		}
	}	
}
