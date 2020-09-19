from django import forms
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from django.utils.safestring import mark_safe
import random
from . import util
import markdown2
from .forms import NewPage, EditPage


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry(request, title):
    if util.get_entry(title) == None:
        raise forms.ValidationError("No such page exists")
    content = markdown2.markdown(util.get_entry(title))
    context = {
        "content" : content,
        "title": title
    }
    return render(request, "encyclopedia/all.html", context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        if util.get_entry(request.GET.get('q')) != None:
            title = request.GET.get('q')
            return HttpResponseRedirect(reverse("wiki:entry", args=(title,)))
        else:
            strings = util.list_entries()
            substring = q
            substrings = [string for string in strings if substring in string]

            context = {
                "query": q,
                "subs": substrings
            }
            return render(request, "encyclopedia/results.html", context)
    else:
        return render(request, "encyclopedia/index.html")

def edit(request, title):
    if request.method == 'POST':
        form = EditPage(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki:entry", args=(title,)))
    instance = util.get_entry(title)
    form = EditPage(initial={'content': instance})
    #form['content'] = content    
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'encyclopedia/edit.html', context)

def new(request):
    if request.method == "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("wiki:entry", args=(title,)))
            else:
                raise forms.ValidationError("Entry with that title already exists")
        else:
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
    return render(request, "encyclopedia/new.html", {
        "form": NewPage()
    })
    
def delete(request, title):
    util.delete_entry(title)
    return HttpResponseRedirect(reverse("wiki:index"))


def random_function(request):
    randomPage = util.list_entries()
    title = random.choice(randomPage)
    return HttpResponseRedirect(reverse("wiki:entry", args=(title,)))


