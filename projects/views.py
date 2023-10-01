from django.shortcuts import render

from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_index.html', context)
