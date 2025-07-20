from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, CourseFile
from .forms import CourseForm, CourseFileForm

def course_list(request):
    courses = Course.objects.all().order_by('-upload_date')
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        file_form = CourseFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')

        if form.is_valid():
            course = form.save()
            for f in files:
                CourseFile.objects.create(course=course, file=f)
            return redirect('courses:course_list')
    else:
        form = CourseForm()
        file_form = CourseFileForm()
    return render(request, 'courses/course_add.html', {'form': form, 'file_form': file_form})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})