from django.shortcuts import render, redirect, get_object_or_404
from .models import InsuranceItem
from .forms import InsuranceItemForm

# Create your views here.

def item_list(request):
    items = InsuranceItem.objects.all()
    return render(request, 'manageData/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = InsuranceItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InsuranceItemForm()
    return render(request, 'manageData/item_form.html', {'form': form})

def item_update(request, insurance_code):
    item = get_object_or_404(InsuranceItem, insurance_code=insurance_code)
    if request.method == 'POST':
        form = InsuranceItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InsuranceItemForm(instance=item)
    return render(request, 'manageData/item_form.html', {'form': form})

def item_delete(request, insurance_code):
    item = get_object_or_404(InsuranceItem, insurance_code=insurance_code)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'manageData/item_confirm_delete.html', {'item': item})