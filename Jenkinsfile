pipeline {
    agent any

    stages {

        stage('build') {
          steps {
              sshagent(credentials: ['	0bb393cf-d60f-49d8-ac60-d5031886dfa5']) {
                sh '''
                    ssh -J quoterback.ru 192.168.10.20
                    'bash -s' < provision_script.sh
                '''
              }
          }
        }
        
    }
}
