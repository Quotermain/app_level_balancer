pipeline {
    agent any


        stage('build') {
          steps {
              sshagent(credentials: ['	0bb393cf-d60f-49d8-ac60-d5031886dfa5']) {
                sh '''
                    ssh -o StrictHostKeyChecking=no -J quoterback.ru 192.168.10.20
                    'bash -s' < provision_script.sh
                '''
              }
          }
        }

    }
}
