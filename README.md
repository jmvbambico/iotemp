# IoTemp #

## Environment ##
- Python 3.7.1
- Redis 3.0.504

## Dependencies ##
- django==2.1.3
- channels==2.1.5
- channels-redis==2.3.1
- asgi_redis==1.4.3
- asgiref==2.3.0
- daphne==2.2.3
- twisted 18.9.0

## Usage ##
1. Ensure redis is running
2. python manage.py runserver
3. Navigate your browser to: http://localhost:8000/thermo/
4. python manage.py readSensor# iotemp
