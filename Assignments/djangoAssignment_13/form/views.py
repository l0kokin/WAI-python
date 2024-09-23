from django.shortcuts import render
from form.forms import UseForm

# Create your views here.
def user_form_view(request):
    if request.method == 'POST':
        form = UseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return render(request, 'form/success.html', {'name': name})
        else:
            return render(request, 'form/form.html', {'form': form})
    else:
        form = UseForm()
        return render(request, 'form/form.html', {'form': form})