from django.shortcuts import render, redirect
from . import models
from . import handlers
# Create your views here.

def main_page(request):
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()
    search_value_from_front = request.GET.get('pr')
    if search_value_from_front:
        all_products = models.Product.objects.filter(name__contains=search_value_from_front)

    context = {'all_categories': all_categories, 'all_products': all_products}
    return render(request, 'models.html', context)

def get_category_products(request, pk):
    # Получить все товары из конкретной категории
    exact_category_products = models.Product.objects.filter(category__id=pk)
    # Передача переменных из бэка на фронт
    context = {'category_products': exact_category_products}
    return render(request, 'category.html', context)

def get_product(request, name, pk):
    get_exact_product = models.Product.objects.get(name=name, id=pk)
    context = {'product': get_exact_product}
    return render(request, 'product.html', context)

def add_pr_to_cart(request,pk):
    # Получить выбранное количество продукта из front части
    quantity = request.POST.get('pr_count')
    product_to_add = models.Product.objects.get(id=pk)
    # Добавление данных
    models.User_Cart.objects.create(user_id=request.user.id, user_product=product_to_add, user_product_quantity=quantity)
    return redirect('/')

def user_cart(request):
    cart = models.User_Cart.objects.filter(user_id=request.user.id)
    context = {'cart': cart}
    return render(request, 'cart.html', context)

def complete_order(request):
    user_cart = models.User_Cart.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        result_message = 'Новый заказ(из E_Shop)\n\n'
        for cart in user_cart:
                result_message += f'Название товаров: {cart.user_product}\n' \
                            f'Количество товаров: {cart.user_product_quantity}\n'
        handlers.bot.send_message(-912319996,result_message)
        user_cart.delete()
        return redirect('/')
    return render(request, 'cart.html', {'cart': user_cart})
def delete_from_user_cart(request, pk):
    user_cart = models.User_Cart.objects.filter(user_id=request.user.id, user_product=pk)
    user_cart.delete()

    return redirect('cart/')