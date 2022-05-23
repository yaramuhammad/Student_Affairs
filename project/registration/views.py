import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django.forms.utils import ErrorList
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail


# Create your views here.

# For default page ----> home page
def home(request):
    return render(request, 'index.html')


# For Contact us page
def contact(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Mobile = request.POST["num"]
        Message = request.POST["msg"]

        msg = 'New Message From ' + Name + '\n' + 'Email: '  + Email +  '\n' + 'Phone: ' + Mobile + '\n' + 'Message: ' + Message

        send_mail("Student Affairs",msg, Email, ['yaramuhammad762@gmail.com'])

        data = ContactUs(FullName=Name, Email=Email, Mobile=Mobile, Message=Message)
        data.save()
    return render(request, 'html/contact-us.html')


# For Department page
def dept(request):
    if request.method == 'GET':
        my_id = request.GET['id']

        existing = AddStudent.objects.filter(pk=my_id, StudentLevel=3).exists() or AddStudent.objects.filter(pk=my_id,
                                                                                                             StudentLevel=4).exists()
        if not existing:
            return render(request, 'html/search.html', {'error': 'DNE'})

        obj = AddStudent.objects.filter(pk=my_id, StudentLevel=3) or AddStudent.objects.filter(pk=my_id, StudentLevel=4)
        context = {
            'student': obj[0],
        }
        return render(request, 'html/dept.html', context)
    elif request.method == 'POST':
        new_dept = request.POST['department']
        stu_id = request.POST['student_id']
        AddStudent.objects.filter(pk=stu_id).update(Department=new_dept)
        return render(request, 'html/search.html')


# For Edit & delete page
def table_view(request):
    result = get_update('All', 'All')
    if request.method == 'POST':
        query = request.POST.get('search', 'All')
        filterVal = request.POST.get('filterVal', 'All')
        result = get_update(query, filterVal)

    return render(request, 'html/edit-delete.html', {'result': result})


# For Registration page
def regist(request):
    if request.method == "POST":
        name = request.POST["username"]
        id = request.POST["ID"]
        gpa = request.POST["gpa"]
        gender = request.POST["gender"]
        birth = request.POST["Date"]
        level = request.POST["Level"]
        active = request.POST["os"]
        system = request.POST["system"]
        prog = request.POST["prog"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]

        data = AddStudent(FullName=name, StudentID=id, Gpa=gpa
                          , Gender=gender, Birth=birth, StudentLevel=level,
                          Status=active, System=system, Department=prog,
                          Email=email, Mobile=mobile
                          )
        data.save()
    return render(request, 'html/Registration.html')


# For Search page
def search(request):
    return render(request, 'html/search.html')


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error-field">%s</div>' % e for e in self])


# For Sing-up page
def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST, error_class=DivErrorList)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'html/student-affairs-home.html')
        else:
            return render(request, 'html/sign-up.html', {"form": form})
    form = NewUserForm(data=None, error_class=DivErrorList)
    return render(request, 'html/sign-up.html', {"form": form})


# For Student Affair Home page
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('affairs-home')
        else:
            messages.error(request, "Invalid Username or Password", extra_tags='inv-user-pass')
    return render(request, 'html/student-affairs-home.html')


def log_out(request):
    logout(request)
    return redirect('affairs-home')


def get_search(request):
    query = request.GET['query']
    if query == 'All':
        result = AddStudent.objects.filter(Status='Active')
    else:
        result = AddStudent.objects.filter(FullName__icontains=query, Status='Active')
        if not result.exists():
            result = AddStudent.objects.filter(StudentID__icontains=query, Status='Active')
            if not result.exists():
                result = AddStudent.objects.filter(Status='Active')
    data = {'result': list(result.values())}
    return JsonResponse(data)


def get_update(query='All', filterVal='All'):
    result = AddStudent.objects.all()
    filterAttr = 'All'
    if '1' <= filterVal <= '4':
        filterAttr = 'StudentLevel'
    elif filterVal == 'Active' or filterVal == 'InActive':
        filterAttr = 'Status'
    elif filterVal == 'MainStream' or filterVal == 'Credit':
        filterAttr = 'System'
    elif len(str(filterVal).split(' ')) == 2:
        filterAttr = 'Department'

    # applying search
    if query != 'All':
        result = AddStudent.objects.filter(FullName__icontains=query)
        if not result.exists():
            result = AddStudent.objects.filter(StudentID__icontains=query)

    # applying filter
    if filterAttr != 'All':
        if filterAttr == 'StudentLevel':
            result = result.filter(StudentLevel=filterVal)
        elif filterAttr == 'System':
            result = result.filter(System=filterVal)
        elif filterAttr == 'Status':
            result = result.filter(Status=filterVal)
        elif filterAttr == 'Department':
            departm = str(filterVal).split(' ')[0]
            print(departm)
            systm = str(filterVal).split(' ')[1]
            print(systm)
            result = result.filter(Department=departm, System=systm)
    return result


def del_student(request):
    id_to_delete = request.GET['id_to_del']
    obj = AddStudent.objects.get(pk=id_to_delete)
    obj.delete()
    return HttpResponse(f"Student with ID: {id_to_delete} deleted successfully.")


def edit_student(request):
    student = json.loads(request.GET['student'])

    stud = AddStudent.objects.filter(pk=student['StudentID']).update(
        FullName=student['FullName'], Status=student['Status'],
        StudentLevel=student['StudentLevel'], Gpa=student['Gpa'], System=student['System'])
    return HttpResponse('Successfully Edited')
