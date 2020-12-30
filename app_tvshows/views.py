from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import Show

def index(request):
    print(request.POST)
    
    return redirect('/shows')

def shows(request):
    context = {
        "shows": Show.objects.all()
    }
    print(Show.objects.all())
    return render(request, "index.html", context)

def newShows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "newShows.html", context)

def processNewShows(request):
    errors = Show.objects.getErrors(request.POST)
    print(errors)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
        
    if request.POST.get('title') and request.POST.get('network') and request.POST.get('release_date') and request.POST.get("description"):
        print("***Creating a new show")
        show = Show()
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        messages.success(request, "Blog successfully updated")
    print(Show.objects.all())
    return redirect('/shows')


# CREATE NEW SHOWS (SYNTAX ERROR)
# def processNewShows(request):
#     Show.objects.create(
#         #title: from the model  #['title']: from form
#         title = request.POST['title'],
#         network = request.POST['network'],
#         release_date = request.POST['release_date'],
#         description = request.POST['description'],
#     )
#     print(request.POST)
#     return redirect('/shows')

def showDetail(request, show_id):
    each_show = Show.objects.get(id=show_id)
    context = {
        'show': each_show
    }
    return render(request, "show_detail.html", context)


def edit(request, show_id):
    each_show = Show.objects.get(id=show_id)
    context = {
        'show': each_show
    }
    return render(request, "edit.html", context)

def processEdit(request, show_id):
    errors = Show.objects.getErrors(request.POST)
    print(errors)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # HOW TO ROUTE TO THE RIGHT PAGE
        # return redirect('/shows' +str(show_id))
        # need to put messages in html after fixing this
        return redirect('/shows/' + str(show_id) + '/edit')
        #or return redirect(f'/shows/{show_id}/edit')
        
    else:
        update_show = Show.objects.get(id=show_id)
        update_show.title = request.POST['title']
        update_show.release_date = request.POST['release_date']
        update_show.network = request.POST['network']
        update_show.description = request.POST['description']
        update_show.save()
        print("saving edits")
        return redirect('/shows')

def delete(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')