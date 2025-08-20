from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboard.forms import ProductForm
from products.models import index_product_details,product_category
from django.contrib.auth.models import User

# Only staff can access
def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def dashboard(request):
# Check that the current user is a staff member for access control
    categories = product_category.objects.all()
    return render(request, 'dashboard/dashboard.html', {'categories': categories})

def category_products(request, category_name):
    products = index_product_details.objects.filter(product_category__name=category_name)
    return render(request, 'dashboard/category_products.html', {'products': products, 'category_name': category_name})


@login_required
@user_passes_test(staff_check)
# Add a new product via the dashboard product form
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_edit_product.html', {'form': form, 'title': 'Add Product'})
def edit_product(request, product_id):
# Edit an existing product from the dashboard
    product = get_object_or_404(index_product_details, product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # or back to category
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/edit_product.html', {'form': form, 'product': product})
def delete_product(request, product_id):
    product = get_object_or_404(index_product_details, product_id=product_id)
# Confirm and delete a product from the dashboard
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')  # or back to category
    return render(request, 'dashboard/delete_product_confirm.html', {'product': product})

from django.views.decorators.http import require_POST

@require_POST
@login_required
@user_passes_test(staff_check)
def update_banner_order(request):
    product_ids = request.POST.getlist('product_ids')
# Update banner ordering for products from dashboard POST data
    for pid in product_ids:
        order_value = request.POST.get(f'banner_order_{pid}')
        product = index_product_details.objects.get(product_id=pid)
        product.banner_order = order_value if order_value else None
        product.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
@user_passes_test(staff_check)
def dashboard_home(request):
    return render(request, 'dashboard/dashboard_home.html')
# Simple dashboard home view for admin welcome page