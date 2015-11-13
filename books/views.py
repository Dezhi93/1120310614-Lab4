# Backstage for search and delete.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book, Author

def search(request):
    error = False
    if 'd' in request.GET:
    	d = request.GET['d']
    	Book.objects.filter(id=d).delete()
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
        	author_id = Author.objects.filter(Name__icontains=q)
        	books = Book.objects.filter(AuthorID__icontains=author_id)
        	return render_to_response('search_results.html',
        		{'books': books, 'query': q})
    return render_to_response('search_form.html',
        	{'error': error})
