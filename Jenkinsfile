node{
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
pip3 install --upgrade pip
ls
pwd
pip3 install -r requirements.txt

#Running unittest

python test.py
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
