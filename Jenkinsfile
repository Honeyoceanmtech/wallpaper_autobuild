pipeline {
  agent any
  stages {
    stage('Git Checkout') {
      steps {
        git branch: 'main', 
            url: '://github.com/Honeyoceanmtech/wallpaper_autobuild.git'
      }
    }
    stage('Deploy')
    {
      steps {
        echo "deploying wallpaper_build"
        sh "docker-compose up --build -d"
      }
    }
  }
}
