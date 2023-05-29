from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NotesForm
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from .models import Notes
from django.http import JsonResponse

# Create your views here.

    # Render form
@login_required
def notes(request):
    form = NotesForm()
    data = Notes.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'notes.html',context)

# Save notes data
@require_http_methods(['POST'])
def save_data(request):
    form = NotesForm(request.POST)
    if form.is_valid():
        id = request.POST.get("id")
        heading = request.POST["heading"]
        content = request.POST["content"]
        if (id == ""):
            note = Notes(heading=heading,content=content)
            note.save()
        else:
            note = Notes(id=id,heading=heading,content=content)
            note.save()
        # Show notes
        note_obtained = Notes.objects.values()
        note_data = list(note_obtained)
        return JsonResponse({'status':1,'note_data':note_data})
    return JsonResponse(form.errors.as_json(),status=404)


# Delete Notes
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Notes.objects.get(id=id)
        note.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
# Edit Data
@require_http_methods(['POST'])
def edit_data(request):
    id = request.POST.get('id')
    note = Notes.objects.get(id=id)
    note_data = {"id":note.id,"heading":note.heading,"content":note.content}
    return JsonResponse({'status':1,'note_data':note_data})