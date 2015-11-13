#coding:utf-8

import sae

from books import wsgi

applicaiton = sae.create_wsgi_app(wsgi.applicaiton)
