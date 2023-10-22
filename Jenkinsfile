pipeline {
	agent any
	stages {
		stage("build") {
			steps {	
				sh 'docker build -t david:latest .'
			}
		}		
		stage("deploy") {
			steps {	
				sh 'docker tag david:latest bit1010/davidtest:latest'
				
				sh 'docker login -u bit1010 -p dckr_pat__Ljf_O9QXl2-tLwadueYD98IoFQ'
				
				sh 'docker push bit1010/davidtest:latest'		
			}
		}
	}		
	post {
		always {
			echo 'building..'
		}
		success {
	    		echo 'success'
			
			sh 'docker rmi bit1010/davidtest:latest'
			sh 'docker rmi david:latest'
		}
		failure {
	    		echo 'failure'
		}
	}
}
