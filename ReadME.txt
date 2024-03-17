Requirements.txt

Installing and settingup virtual environment

1.To install virtual environment

>>>pip install virtualenv

2.Creating virtual environment

>>>virtualenv myenv

3.To activate virtual environment

>>>myenv\Scripts\activate


Installation of python packages inside this virtual environment

1.Installing Django

>>>pip install django

2.Installing MYSQL client

>>>pip install mysqlclient

3.Installing nmap library

>>>pip install python-nmap

4.Installing zap library

>>>pip install python-owasp-zap-v2.4

5.Installing pika library

>>>pip install pika

Installation of zap tool

-Download Zap from official website and install its setup and add its bin folder to environment variable.

Installation of RabbitMQ

-Install RabbitMQ from official website and add its bin folder to environment variable
-use this command to run RabbbitMQ on browser

>>>rabbitmq-plugins enable rabbitmq_management

Installation of MYSQL

-Install MYSQL from official website and add its bin folder to environment variable.


How to setup running environment

1.Create virtual environment and install django, mysqlclient, zap, nmap and pika.
2.Open Zap application and in Tools->options->ApI you could find ApI key copy it and replace it in utils->terminal->zap.py api_key="your_api_key"
3.Run RabbitMQ on browser using this URL->  http://localhost:15672

Running Project

1.Navigate to folder where manage.py is present and execute the below command

>>>python manage.py runserver 

2.Now the project will start running on http://127.0.0.1:8000/ , you could type this link in browser to run this application in a local server.

3.To break server press ctrl+C.





