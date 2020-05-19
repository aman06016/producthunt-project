from django.shortcuts import render
from django.http import HttpResponse as ht
from genre.models import Genre
from .models import Selfhelp
from django.shortcuts import get_object_or_404
# Create your views here.



def booklist(request,book_id):
    title=Genre.objects.filter(id=book_id)

    if(book_id==1):
        books=Selfhelp.objects.filter(genre__contains=title[0].title)
        return render(request,'booktypes/selfhelp.html',{'books':books})
        #return ht(books[0].book_name)
    elif(book_id==2):
        books=Selfhelp.objects.filter(genre__contains=title[0].title)
        return render(request,'booktypes/bussiness.html',{'books':books})
    elif(book_id==3):
        books=Selfhelp.objects.filter(genre__contains=title[0].title)
        return render(request,'booktypes/history.html',{'books':books})
    elif(book_id==4):
        books=Selfhelp.objects.filter(genre__contains=title[0].title)
        return render(request,'booktypes/fiction.html',{'books':books})
    else:
        books=Selfhelp.objects.filter(genre__contains=title[0].title)
        return render(request,'booktypes/investing.html',{'books':books})

def bookdetail(request,onebook_id):
    book_ob=get_object_or_404(Selfhelp,pk=onebook_id)
    return render(request,'booktypes/book_detail.html',{'onebook':book_ob})
    #return ht("dfgsd")
