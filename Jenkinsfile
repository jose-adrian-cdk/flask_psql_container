pipeline {
  agent any
  stages {
    stage('setup') {
      steps {
        sh 'docker -v'
      }
    }

    stage('install') {
      steps {
        sh 'docker'
      }
    }

    stage('deploy') {
      steps {
        sh 'docker build -t web_server:1.0 services/web/'
      }
    }

    stage('run') {
      steps {
        sh 'docker run -itd --rm --name web_server_cont -p 5000:5000 web_server:1.0'
      }
    }

  }
}