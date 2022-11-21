from django.shortcuts import render
from t_test_app.forms import NewEntryForm


# Create your views here.


# from statistics_app.

# Create your views here.
def index(request):
    form = NewEntryForm()
    if request.method == "POST":
        # form.save(commit=True)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error... Form invalid')
    return render(request, 't_test_app/index.html', {'form': form})

# def other(request):
#     return render(request, 'statistics_app/other.html')


# def relative(request):
#     return render(request, 'statistics_app/relative_url_templates.html')

#
# def entry_form_view(request):
#     form = forms.EntryForm()
#     return render(request, 'statistics_app/form_page.html', {'form': form})
