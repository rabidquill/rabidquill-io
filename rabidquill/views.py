import datetime
import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from rabidquill.models import Document


def home(request):
    return render(request, "home.html")


def login_view(request):
    print(request)
    if request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render(request, "login.html", c)
    if request.method == "POST":
        user = None
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                # the password verified the user
                if user.is_active:
                    login(request, user)
                    return redirect("/documents")
                else:
                    print("The password is valid but the user is inactive.")
            else:
                # unable to verify username or password
                print("Username and password were incorrect.")
        except Exception as exc:
            print("Something went wrong. {0}".format(exc.message))


@login_required
def logout_view(request):
    try:
        logout(request)
    except Exception as exc:
        print("Problem logging out: {0}".format(exc.message))
    return redirect("/")


@login_required
def documents(request):
    if request.method == "POST":
        if request.POST['title']:
            newdoc = Document.objects.create(
                author=request.user,
                created=datetime.datetime.now(),
                modified=datetime.datetime.now(),
                directory_id=1,
                title=request.POST['title'])
            newdoc.save()

    docs = Document.objects.all().filter(author=request.user)
    c = dict(documents=docs)
    c.update(csrf(request))
    return render(request, "documents.html", c)


@login_required
def delete(request, id):
    doc = Document.objects.all().filter(author=request.user, id=id)
    doc.delete()
    return redirect("/documents")


@login_required
def edit(request, document):
    doc = Document.objects.get(author=request.user, id=document)
    if request.method == "POST":
        doc.body = request.POST['content']
        doc.modified = datetime.datetime.now()
        doc.save()
        return HttpResponse(json.dumps(dict(success=True)))

    c = {"document": doc}
    c.update(csrf(request))
    return render(request, "editor.html", c)