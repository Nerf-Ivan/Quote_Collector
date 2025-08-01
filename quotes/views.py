from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote
from .forms import QuoteForm

def quote_list(request):
    quotes = Quote.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to DB
            return redirect('quote_list')  # Redirect to avoid form resubmission
    else:
        form = QuoteForm()

    return render(request, 'quotes/quote_list.html', {
        'quotes': quotes,
        'form': form
    })

def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quotes/edit_quote.html', {'form': form})


def delete_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        return redirect('quote_list')
    return render(request, 'quotes/delete_quote.html', {'quote': quote})

# quotes/views.py
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
