from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projectsObj, results):
    page = request.GET.get('page')  # 1
    paginator = Paginator(projectsObj, results)

    try:
        projectsObj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projectsObj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projectsObj = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projectsObj


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)  # name__iexact

    projectsObj = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) | Q(tags__in=tags)
    )

    return projectsObj, search_query
