from django.shortcuts import render
from .models import Profile 
import pdfkit
from django.http import HttpResponse 
from django.template import loader 
import io 
# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        college = request.POST.get("college","")
        university = request.POST.get("university","")
        experience = request.POST.get("experience","")
        skills = request.POST.get("skills","")
        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,college=college,university=university,experience=experience,skills=skills)
        profile.save()
    return render(request,'pdf/accept.html')

def cv(request,id):
    user_profile = Profile.objects.get(id=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf) 
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response