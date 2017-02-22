node{
stage('Build')
{
    sh '''
#Deployment Virtualenv

virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt

#Running unittest

python test.py
    '''
}
stage('Collect QA Test Results')
{
    junit 'test-reports/*'
}
stage('Deploy')
{

echo 'Deploy'

}

}
