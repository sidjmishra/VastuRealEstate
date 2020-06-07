from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.shortcuts import render
from .models import Property_Information,PropertyImage
from marketing.models import Subscription

def index(request):
    latest = Property_Information.objects.order_by('-timestamp')[0:3]
    property_list = Property_Information.objects.all()
    paginator = Paginator(property_list,3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        email = request.POST.get('email', '')

        send_mail('Rgistration of user', # subject
        'Email Body', # mail body
        email, # sender mail
        ['noddymishracr7@gmail.com'], # receiver mail
        fail_silently = False
        )

        new_subscription = Subscription()
        new_subscription.email = email
        new_subscription.save()

    context = {
        'latest': latest,
        "queryset":paginated_queryset,
        "page_request_var":page_request_var,
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        send_mail(subject, # subject
        message, # mail body
        email, # sender mail
        ['noddymishracr7@gmail.com'], # receiver mail
        fail_silently = False
        )
    return render(request, 'contact.html',{})

def properties(request):
    property_list = Property_Information.objects.all()
    paginator = Paginator(property_list,3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        "queryset":paginated_queryset,
        "page_request_var":page_request_var,
    }
    return render(request, 'property-grid.html',context)

def property_detail(request,id):
    propertY = get_object_or_404(Property_Information, id=id)
    photos = PropertyImage.objects.filter(propertY=propertY)
    context = {
        'propertY':propertY,
        'photos':photos,
    }
    return render(request, 'property-single.html',context)
