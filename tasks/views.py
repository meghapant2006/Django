
from django.shortcuts import render

tasks = ["megha", "john", "doe"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })