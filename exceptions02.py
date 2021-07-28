import urllib
import urllib.request
 
try:
     site = urllib.request.urlopen('http://corndog.io/')
except:
    print('Site indisponível.')
else:
    print('Site acessado com sucesso.')
    print(site.read())
    
    
 