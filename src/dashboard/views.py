from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboard.forms import ProductForm
from products.models import index_product_details

# Only staff can access
def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def dashboard(request):
    products = index_product_details.objects.all()
    return render(request, 'dashboard/dashboard.html', {'products': products})

@login_required
@user_passes_test(staff_check)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_edit_product.html', {'form': form, 'title': 'Add Product'})

@login_required
@user_passes_test(staff_check)
def edit_product(request, pk):
    product = get_object_or_404(index_product_details, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/add_edit_product.html', {'form': form, 'title': 'Edit Product'})

@login_required
@user_passes_test(staff_check)
def delete_product(request, pk):
    product = get_object_or_404(index_product_details, pk=pk)
    product.delete()
    return redirect('dashboard')
