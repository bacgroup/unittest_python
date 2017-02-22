node{
    stage('Prepare')
    {
        ws{
            deleteDir()
        }
    }
    stage('Integrate')
    {
        git 'https://github.com/bacgroup/unittest_python.git'
    }
    stage('Build')
    {
        sh '''
#Deployment Virtualenv

virtualenv -p python3 env
. env/bin/activate
which python
#pip install --upgrade pip
ls
pwd
pip install -r requirements.txt
deactivate
#Running unittest
echo `python test.py`
        '''
    }
    stage('Q/A Test Results')
    {
        junit 'test-reports/*'
    }
    stage('Deploy')
    {
        echo 'Deploy'

    }
}
