from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal
from .forms import GoalForm
from django.contrib.auth.decorators import login_required

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user).order_by('deadline')
    return render(request, 'goals/goal_list.html', {'goals': goals})

@login_required
def goal_add(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/goal_add.html', {'form': form})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/goal_update.html', {'form': form, 'goal': goal})