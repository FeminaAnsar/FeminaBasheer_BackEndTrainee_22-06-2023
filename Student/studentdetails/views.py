from django.shortcuts import render
from .forms import StudentForm
from django.shortcuts import redirect


def home(request):
    return render(request,'studentdetails/home.html')

def student(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(student)
    else:
        form=StudentForm()

    return render(request,"studentdetails/student.html",{"form":form})


# Create your views here.
