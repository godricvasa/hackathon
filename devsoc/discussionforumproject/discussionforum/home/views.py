from django.shortcuts import render, HttpResponse
from .forms import UserProfileForm

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added successfully')  # Redirect to a success page
    else:
        form = UserProfileForm()
    return render(request, 'index.html', {'form': form})

