HelloDjango
===========

say hello to django in eclipse

tip:
in eclipse hide pyc files {
	ctrl+f10 in your project
	filter -> add "*.pyc"
}



httpd.conf:
==>
LoadModule wsgi_module modules/mod_wsgi-win32-ap22py27-3.3.so
WSGIScriptAlias / D:/workspace/indigo/HelloDjango/django.wsgi
<Directory "D:/workspace/indigo/HelloDjango">
    AllowOverride None
    Options None
    Order allow,deny
    Allow from all
</Directory>
==>;
