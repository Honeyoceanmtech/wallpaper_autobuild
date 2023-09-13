pipeline {
  agent any
  stages {
    stage('Git Checkout') {
      steps {
        git branch: 'main', 
            url: 'https://github.com/Honeyoceanmtech/wallpaper_autobuild.git',
            changelog: true,
      }
    }
    stage('Deploy')
    {
      steps {
        echo "deploying wallpaper_build"
        sh "docker-compose up"
      }
    }
  }
}
