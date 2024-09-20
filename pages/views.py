from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Event
from django.db import connection

@login_required
def home_view(request):
    events = Event.objects.all()
    return render(request, "index.html", {"events": events, "user": request.user})

@login_required
def add_event_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        title = request.POST.get('title')
        
        if not date or not starttime or not endtime or not title:
            return redirect('/add_event')
        if int(starttime) >= int(endtime):
            return redirect('/add_event')
        if int(starttime) < 0 or int(starttime) > 24 or int(endtime) < 0 or int(endtime) > 24:
            return redirect('/add_event')
        
        events = Event.objects.filter(date=date)

        for event in events:
            if int(starttime) >= event.starttime and int(endtime) <= event.endtime:
                return redirect('/add_event')
            if int(starttime) <= event.starttime and int(endtime) >= event.endtime:
                return redirect('/add_event')
            if int(endtime) < event.endtime and int(endtime) > event.starttime:
                return redirect('/add_event')
            if int(starttime) < event.endtime and int(starttime) > event.starttime:
                return redirect('/add_event')
            
        try:
            Event.objects.create(date=date, starttime=starttime, endtime=endtime, created_by=request.user, title=title)
            return redirect('/')
        except:
            return redirect('/add_event')

    return render(request, "add_event.html")

@login_required
def delete_event_view(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
    except:
        pass
    return redirect('/')

@login_required
def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query:
            sql = f"SELECT id, title, date, starttime, endtime FROM pages_event WHERE title LIKE '%{query}%'"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                events = [
                {"id": r[0], "title": r[1], "date": r[2], "starttime": r[3], "endtime": r[4]}
                for r in results]
        else:
            events = []
        return render(request, 'search_results.html', {"events": events})

    return render(request, 'search_events.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create_user(username=username, password=password)
            return redirect('/login')
        except:
            return redirect('/register')

    return render(request, "register.html")