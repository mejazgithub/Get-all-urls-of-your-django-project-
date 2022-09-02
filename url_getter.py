import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
import django
django.setup()

from urls import urlpatterns #this import should be inside the function to avoid an import loop

def get_urls(raw_urls, nice_urls=[], urlbase=''):
    for entry in raw_urls:
        fullurl = (urlbase + str(entry.pattern)).replace('^','')
        if entry.callback: #if it points to a view
            nice_urls.append(fullurl)
        else: #if it points to another urlconf, recur!
            get_urls(entry.url_patterns, nice_urls, fullurl)
    return nice_urls


nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

# for i,path in enumerate(nice_urls): 
#     if 'api/' in str(path): 
#         print(path)
