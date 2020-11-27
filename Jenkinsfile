pipeline {
  agent any
  stages {
    stage('setup') {
      steps {
        echo 'Hello world'
        sh 'env'
      }
    }

    stage('install') {
      steps {
        sh 'gcc -v '
      }
    }

  }
}