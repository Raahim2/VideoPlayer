from django.shortcuts import render , redirect
from .models import Doctor , Patient
from ctransformers import AutoModelForCausalLM
# face - 1@3

current_user = None

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if(request.method=='POST'):
        usrename = request.POST.get('usr')
        password = request.POST.get('pass')

        user = Patient.objects.filter(username = usrename , password=password)
        print(user)

        if(user):
            print(user)
            global current_user
            current_user = user
            return redirect('/dashboard')

        else:
            message = "Please Enter Correct Usrename Or Password"
            return render(request, 'login.html' , {'message': message})
        
    return render(request,'login.html')

def signup(request):
    if(request.method=='POST'):
        print("Form sub")
        usrename = request.POST.get('usr')
        password = request.POST.get('pass')
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        full_name = fn + " " + ln
        age = request.POST.get('age')
        bg = request.POST.get('bg')
        gender = request.POST.get('gender')

        new_patient = Patient.objects.create(username=usrename , password = password , name =full_name , bg=bg , gender=gender , age=age)
        
        new_patient.save()

        print(f"name = {fn + ln}\n usrename = {usrename}\npass={password}, \n{age}\n{bg}\n{gender}")

    return render(request,'signup.html')

def dashboard(request):
    if(current_user==None):
        return render(request , 'login.html' )
    return render(request , 'dashboard.html' , {'current_user': current_user})

def appoint(request):
    if(current_user==None):
        return render(request , 'login.html' )
    return render(request , 'appoint.html' , {'current_user': current_user})

def report(request):
    
    if(current_user==None):
        return render(request , 'login.html' )


    if(request.method=='POST'):
        
        disease = request.POST.get('disease')
        
        # path = 'chatbot'
        chatbot = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.2-GGUF")

        reply = chatbot(f"Question : What is {disease}  Answer : " , stop=['Question'] )
        print(reply)
        return render(request , 'report.html' , {'current_user': current_user , 'generated':reply})

    return render(request , 'report.html' , {'current_user': current_user })


