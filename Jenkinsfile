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
        sh 'docker build -t web_server:1.0'
      }
    }

  }
}