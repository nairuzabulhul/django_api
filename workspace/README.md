
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

Steps to create Djnago Restful Api:

1- install pip

  sudo easy_install pip


2- Intstall Django rest framework

  sudo pip install djangorestframework


3- create a new app

    python manage.py startapp new_APP
    
    
4- Add the restframwork with your app name to the settings.py

    'rest_framework',
    'new_APP'
    
5- Create a model for your data


6- Create a new file serializer.py to convert data to JSON objects


7- 