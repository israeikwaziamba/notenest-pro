from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def grade_list(request):
    notes = Note.objects.all()
    return render(request, 'grades/grade_list.html', {'notes': notes})

def grade_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = NoteForm()
    return render(request, 'grades/grade_add.html', {'form': form})

def grade_stats(request):
    notes = Note.objects.all()
    total_points = sum(n.valeur * n.coefficient for n in notes)
    total_coeffs = sum(n.coefficient for n in notes)
    moyenne = total_points / total_coeffs if total_coeffs > 0 else 0
    return render(request, 'grades/grade_stats.html', {
        'moyenne': round(moyenne, 2),
        'notes': notes
    })