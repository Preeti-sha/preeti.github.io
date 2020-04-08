from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
#from RESUMEAPP.forms import ResumeForm
from .models import *

from docx import Document
import json


# Create your views here.
def getUserDetails(request):
    # get the doc/docx file from the input field in first page and parse it here and then on
    # click of submit pass it as model object to second page which is Resume.html
    # find how to use post and how to parse the data
    userData = UserDetailsModel.objects.all()
    print("Inside getUserDetails")
    context = {
        'userData': userData
    }
    return render(request, 'FUNNY/first.html', context)


def upload(request):
    print('output')
    print("Open second page")
    # return render(request,'RESUMEAPP/Resume.html')
    return render(request, 'FUNNY/second.html')


def UserDetails(request):
    print("Upload File xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if request.method == 'POST':
        # Extract the document from filesystem
        document = Document('C:/Users/Tanmaay/PycharmProjects/HP/FUNNY/ResumeTemp1.docx')
        document.save('res.docx')

        bolds = []
        vals = []
        data = {}

        # Read the document in python :paragraph parsing
        for para in document.paragraphs:
            print(para.text)
            for run in para.runs:
                if run.bold:
                    strText = run.text
                    colPos = strText.index(':')
                    if colPos > 0:
                        keyStr = run.text[:colPos - 1]
                        bolds.append(keyStr.replace(' ', '_').lower())
                else:
                    vals.append(run.text.strip())

        for index in range(len(bolds)):
            data[bolds[index]] = vals[index]

        json_data = json.dumps(data)
        print('Json Data: ', json_data)

        return render(request, 'FUNNY/second.html', {'dataset': data})
    else:
        print("else")


def saveUserDetails(request):
    if request.method == 'POST':
        firstName = request.POST['First_Name']
        lastName = request.POST['Last_Name']
        emailId = request.POST['Email_Id']
        contactNo = request.POST['Mobile_Number']
        streetAddress = request.POST['Address']
        city = request.POST['City']
        state = request.POST['State']
        country = request.POST['Country']
        zipCode = request.POST['Pin_Code']
        workStatus = request.POST['workstatus']
        education = request.POST['education']
        skillSet = request.POST['skill']
        workExp = request.POST['exp']
        print("inside post")

        usermodel = UserDetailsModel.objects.create(firstName=firstName, lastName=lastName, emailId=emailId,
                                                    contactNo=contactNo, streetAddress=streetAddress,
                                                    city=city, state=state, country=country, zipCode=zipCode,
                                                    workStatus=workStatus, education=education,
                                                    skillSet=skillSet, workExp=workExp)
        usermodel.save()

        return render(request, 'FUNNY/save.html')
    else:
        print("else")


def saveUserDetailsOld(request):
    # userShow = UserDetailsModel.objects
    form = ResumeForm()
    submitted = False
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            usermodel = UserDetailsModel(
                firstName=form.cleaned_data["fName"],
                lastName=form.cleaned_data["lName"],
                emailId=form.cleaned_data["emailid"],
                contactNo=form.cleaned_data["contact"],
                streetAddress=form.cleaned_data["street"],
                city=form.cleaned_data["city"],
                state=form.cleaned_data["state"],
                country=form.cleaned_data["country"],
                zipCode=form.cleaned_data["zipcode"],
                workStatus=form.cleaned_data["workstatus"],
                education=form.cleaned_data["education"],
                skillSet=form.cleaned_data["skillset"],
                workExp=form.cleaned_data["workexp"],
            )
            usermodel.save()
            print("saving data")
            return redirect('/save.html')
        else:
            form = ResumeForm()
            if 'submitted' in request.GET:
                submitted = True
    usermodel = UserDetailsModel.objects.all()
    context = {
        "usermodel": usermodel,
        "form": form,
        'submitted': submitted,
    }
    # return render(request, "RESUMEAPP/Resume.html", context)
    return render(request, 'FUNNY/Resume.html', context)


"""
def hi(request):
    return render(request,'FUNNY/second.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

    """

