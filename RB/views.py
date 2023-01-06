from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from django.conf import settings
# from django.core import mail
# from django.core.mail.message import EmailMessage
# from weasyprint import HTML
from .connection import Mongopy
from .forms import TemplateForm, CoverForm
from .models import ResumeData, Contact, CoverLetter
from .utils import render_to_pdf


# Create your views her

def home(request):
    form = UserCreationForm()
    data = {'form': form}
    return render(request, 'resumeHome/home.html', data)


def reg(request):
    fm = UserCreationForm()
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            messages.error(request, "Password doesn't match!!")
            return redirect("/")
        try:
            if User.objects.get(username=username):
                messages.warning(request, "Username is already taken!")
                return redirect("/")

        except Exception:
            pass
        user = User.objects.create_user(username=username, password=pass1)
        user.save()
        messages.success(request, "SignUp Successful!")
        return redirect("/")

    return render(request, 'resumeHome/navbar.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_pass']
        print("USER NAME IS   ", email, password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(email, password)
            messages.success(request, f"Welcome! {email}")
            m = Mongopy()
            m.connect('name')

            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            print("........No.........")
            return redirect("/")

    return redirect("/")


def contact(request):
    print("request")
    if request.method == "POST":
        c = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        message = request.POST.get('msg')
        c.name = name
        c.email = email
        c.phoneno = phoneno
        c.msg = message
        c.save()

        # from_email = settings.EMAIL_HOST_USER
        # conn = mail.get_connection()
        # conn.open()
        # email_message = mail.EmailMessage(f'Email From {name}',
        #                                   f'User Email :{email} '
        #                                   f'\n User Phone Number:{phoneno} \n '
        #                                   f'Message from User: {message}',
        #                                   from_email, ['keyurninama27@gmail.com'], connection=conn)
        #
        # email_message_user = mail.EmailMessage(f'ResumeUp Response',
        #                                        f'Hey {name}\n\n Thanks for reaching us. \n '
        #                                        f'we will get back to you soon',
        #                                        from_email, [email], connection=conn)
        #
        # conn.send_message([email_message, email_message_user])
        # conn.close()

        messages.info(request, "Your response has been recorded. Thanks for reaching us.")
        return redirect("/")
    return render(request, 'resumeHome/contact.html')


def user_logout(request):
    logout(request)
    return redirect("/")


def user_resume(request):
    return render(request, 'resumeHome/resumehome.html')


def user_cv(request):
    return render(request, 'resumeHome/cvhome.html')


def get_demo(request, id):
    return render(request, 'resumeTemplates/template' + str(id) + '.html')


def get_blog(request, id):
    return render(request, 'blog/blog' + str(id) + '.html')


def get_form(request, id):
    print("user is ", request.user.email)
    return render(request, 'formTemplate/form1.html', {'id': id})


def get_cover_form(request, id):
    print("user is ", request.user.email)
    return render(request, 'formTemplate/form2.html', {'id': id})


def resume_form(request, id):
    fm = TemplateForm(request.POST)
    print("name is ", fm['name'].value())

    resumedata = ResumeData(request.POST)

    name = request.POST.get('name')
    email = request.POST.get('email')
    prof = request.POST.get('prof')
    college = request.POST.get('college')
    college_join = request.POST.get('college_join')
    college_leave = request.POST.get('college_leave')
    college_field = request.POST.get('college_field')
    college_per = request.POST.get('college_per')
    school_12 = request.POST.get('school_12')
    school_12_join = request.POST.get('school_12_join')
    school_12_leave = request.POST.get('school_12_leave')
    school_12_field = request.POST.get('school_12_field')
    school_12_per = request.POST.get('school_12_per')
    school_10 = request.POST.get('school_10')
    school_10_join = request.POST.get('school_10_join')
    school_10_leave = request.POST.get('school_10_leave')
    school_10_per = request.POST.get('school_10_per')
    skill_name_1 = request.POST.get('skill_name_1')
    skill_1 = request.POST.get('skill_1')
    skill_name_2 = request.POST.get('skill_name_2')
    skill_2 = request.POST.get('skill_2')
    skill_name_3 = request.POST.get('skill_name_3')
    skill_3 = request.POST.get('skill_3')
    project = request.POST.get('project')
    project_obj = request.POST.get('project_obj')
    project_tech = request.POST.get('project_tech')
    resumedata.name = name
    resumedata.email = email
    resumedata.prof = prof
    resumedata.college = college
    resumedata.college_join = college_join
    resumedata.college_leave = college_leave
    resumedata.college_field = college_field
    resumedata.college_per = college_per
    resumedata.school_12 = school_12
    resumedata.school_12_join = school_12_join
    resumedata.school_12_leave = school_12_leave
    resumedata.school_12_field = school_12_field
    resumedata.school_12_per = school_12_per
    resumedata.school_10 = school_10
    resumedata.school_10_join = school_10_join
    resumedata.school_10_leave = school_10_leave
    resumedata.school_10_per = school_10_per
    resumedata.skill_name_1 = skill_name_1
    resumedata.skill_1 = skill_1
    resumedata.skill_name_2 = skill_name_2
    resumedata.skill_2 = skill_2
    resumedata.skill_name_3 = skill_name_3
    resumedata.skill_3 = skill_3
    resumedata.skill_name_3 = skill_name_3
    resumedata.project = project
    resumedata.project_obj = project_obj
    resumedata.project_tech = project_tech

    data = {'form': fm}
    resumedata.save()
    print("................")
    return render(request, 'getResumeTemplate/form' + str(id) + '.html', data)


def cover_form(request, id):
    fm = CoverForm(request.POST)
    cv = CoverLetter(request.POST)
    print("name is ", fm['name'].value())
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    prof = request.POST.get('prof')
    purpose = request.POST.get('purpose')
    study = request.POST.get('study')
    strength = request.POST.get('strength')
    experience = request.POST.get('experience')

    cv.name = name
    cv.email = email
    cv.phone = phone
    cv.job = prof
    cv.purpose = purpose
    cv.study = study
    cv.strength = strength
    cv.exp = experience

    data = {'form': fm}
    cv.save()
    print("................")

    return render(request, 'getResumeTemplate/form' + str(id) + '.html', data)


def blog(request):
    return render(request, 'resumeHome/blogHome.html')


def privacy(request):
    return render(request, 'resumeHome/privacy.html')


def about(request):
    return render(request, 'resumeHome/about.html')


def dowpdf():
    user = ResumeData(name='{name}')
    print("..........................")
    data = {
        'form': user
    }
    pdf = render_to_pdf('resumeTemplates/template5.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def saved_resume(request):
    profile = ResumeData.objects.all()
    return render(request, 'getSavedTemplate/savedResume.html', {'profile': profile})

# return render(request, "getSavedTemplate/savedResume.html")
