from django.shortcuts import render, get_object_or_404
from products.models import Category, index_product_details


def ecommerce(request, category_name=None): 
    categories = Category.objects.all()  # Fetch all categories for navigation

    # Default to the first category if no category is provided
   
    category = get_object_or_404(Category, name=category_name) if category_name else categories.filter(name="Appliances").first()

    # Filter products by the selected category
    products = index_product_details.objects.filter(category=category)

    return render(request, 'index.html', {'products': products, 'categories': categories, 'selected_category': category})
