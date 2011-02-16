##django-infochimps

This simple Django application retrieves Twitter metrics provided by Infochimps and graphs them using the Google Chart API. To learn about the Infochimp TrstRank (TR) and TrstQuotient (TQ) scores, please visit [Infochimps](http://api.infochimps.com/describe/soc/net/tw/trstrank).

#### Requirements
To run this you'll need Django 1.1.1 or greater. Check your version:

    >> import django    
    >> django.VERSION   
    (1, 1, 1, 'final', 0)   

If necessary, install or upgrade Django:

    $ pip install Django==1.1.1 
    
You also need [infochimpy](https://github.com/gerlad/django-infochimps)
    
    $ git clone git@github.com:gerlad/infochimpy.git 
    $ cd infochimpy  
    $ python setup.py install    
    
Then git and run:

    $ git clone git@github.com:gerlad/django-infochimps.git 
    $ cd django-infochimpy  
    $ python manage.py runserver    