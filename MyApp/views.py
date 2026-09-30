from django.shortcuts import render, redirect
from .models import Reminder
from .forms import ReminderForm


def reminder_list(request):
    reminders = Reminder.objects.all().order_by('date', 'time')

    return render(request, 'MyApp/reminders_list.html', {
        'reminders': reminders
    })


def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reminder_list')

    else:
        form = ReminderForm()

    return render(request, 'MyApp/reminder_form.html', {
        'form': form
    })