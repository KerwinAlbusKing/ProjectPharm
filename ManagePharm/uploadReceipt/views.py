from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReceiptImageForm
from .models import Receipt

@login_required
def upload_receipt_view(request):
    # 사용자 영수증 모델 생성 (없으면 생성)
    if not hasattr(request.user, 'receipt'):
        Receipt.objects.create(user=request.user)

    if request.method == 'POST':
        form = ReceiptImageForm(request.POST, request.FILES, instance=request.user.receipt)
        if form.is_valid():
            form.save()
            return redirect('receipt_success')
    else:
        form = ReceiptImageForm(instance=request.user.receipt)

    return render(request, 'uploadReceipt/upload_receipt.html', {'form': form})

def receipt_success_view(request):
    return render(request, 'accounts/home.html')