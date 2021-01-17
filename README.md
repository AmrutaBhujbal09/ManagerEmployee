# ManagerEmployee
Manager Employee Portal

Awesome web-browsable Web APIs.

Overview

    Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

The Web browsable API is a huge usability win for your developers.
Authentication policies including optional packages for OAuth1a and OAuth2.
Serialization that supports both ORM and non-ORM data sources.
Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
Extensive documentation, and great community support.


Below: Screenshot from the browsable API



Requirements
Python (3.9)
Django (3.1)
.

Installation
Install using pip...


pip install djangorestframework ,
pip intsall mysqlclient ,
Add 'rest_framework' to your INSTALLED_APPS setting.



 [
    
    ...
    'rest_framework',
]
Example
Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups



Startup up a new project like so...

pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
Now edit the example/urls.py module in your project:

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers,  views, routers

# Serializers define the API representation.


class UserSignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
    
        # model name
        model=User
        fields=["first_name","last_name","password","email","username","address","dob","company",
                ]
                
# View,py define the view behavior.
    
    class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer






# Wire up our API using automatic URL routing.

from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('manager/',include('manager_app.urls')),
    path('employee/',include('employee_app.urls'))
]
We'd also like to configure a couple of settings for our API.

Add the following to your settings.py module:



INSTALLED_APPS = [
    
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

That's it, we're done!

./manage.py runserver
You can now open the API in your browser at http://127.0.0.1:8000/, and view your new 'users' API. If you use the Login control in the top right corner you'll also be able to add, create and delete users from the system.

You can also interact with the API using command line tools such as curl. For example, to list the users endpoint:
Or to create a new user:


Documentation & Support
Full documentation for the project is available at https://www.django-rest-framework.org/.

For questions and support, use the REST framework discussion group, or #restframework on freenode IRC.

You may also want to follow the author on Twitter.

Security
Please see the security policy.

About
Web APIs for Django. 🎸

www.django-rest-framework.org
Topics
python api django rest
Resources
 Readme
License
 View license
Releases 124
Version 3.9.3
Latest
Apr 29, 2019
+ 123 releases
Sponsor this project
https://fund.django-rest-framework.org/topics/funding/
Packages
No packages published
Used by 187k
@rohan9769
@tharcissie
@ArtemVolik
@8490
@zahirekrem09
@Rouvas
@aghyadalbalkhi-ASAC
@furkan-cloud
+ 187,062
Contributors 1,031
