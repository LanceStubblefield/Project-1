from django import forms
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, redirect
from . import util
import re
import random

# class NewEntryForm(forms.Form):
#     entry = forms.CharField(label="New Entry")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    casefold()
    return HttpReponseRedirect(request,"encyclopedia/random.html"


def error(request):
    return render(request, "encyclopedia/error.html")


def title(request):
    return render(request, "encyclopedia/title.html", {
        "new": util.get_entry(f"entries/{title}.md")
    })


def create(request):
    return render(request, "encyclopedia/create.html", {
        # "form": NewEntryForm()
    })


def random(request):
    page_list = [(f"entries/{title}.md")]
    random.choice(page_list)

    return HttpReponseRedirect(reverse("title", args=(title,))),"encyclopedia/random.html")


def edit(request):
    return render(request, "encyclopedia/edit.html")
