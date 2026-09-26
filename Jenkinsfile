pipeline { agent any; stages { stage('Test'){ steps { sh 'pytest -q' } } stage('Build'){ steps { sh 'docker build -t netmon .' } } } }
