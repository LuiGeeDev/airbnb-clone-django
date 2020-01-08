from django.utils import timezone
from django.shortcuts import render

# Create your views here.
def all_rooms(request):
    now = timezone.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
