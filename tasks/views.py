from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.order_by("-created_at", "-pk")

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
    })


def task_create(request):
    form = TaskForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:list")

    return render(request, "tasks/task_create.html", {
        "form": form,
    })


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, "tasks/task_detail.html", {
        "task": task,
    })


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])

    if request.POST.get("return_to") == "detail":
        return redirect("tasks:detail", pk=pk)

    return redirect("tasks:list")