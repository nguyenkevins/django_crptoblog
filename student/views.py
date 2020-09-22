from django.shortcuts import render, redirect
from student.forms import StudentForm
from student.models import Student
import csv

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
def show(request):
    students = Student.objects.all()
    return render(request,"show.html",{'students':students})
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html', {'student':student})
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'student': student})
def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")
def export(request):
    students = Student.objects.all()

    with open('record.csv', mode='w', newline='') as record_file:
        record_writer = csv.writer(record_file, skipinitialspace=True, delimiter=',', quotechar='"',
                                        quoting=csv.QUOTE_MINIMAL)
        record_writer.writerow(
            ["Student Grade", "Student First Name", "Student Last Name", "Parent/Guardian First Name", "Parent/Guardian Last Name", "Student Email", "Student Contact"])
        for student in students:
            record_writer.writerow([student.sid, student.sfname, student.slname, student.gfname, student.glname, student.semail, student.scontact])

    return render(request, "show.html", {'students': students})
def clear(request):
    students = Student.objects.all()
    students.delete()
    return render(request, "show.html", {'students': students})