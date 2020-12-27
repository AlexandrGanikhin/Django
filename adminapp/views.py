from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import Product, ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, UserAdminCreateProductForm


@user_passes_test(lambda user: user.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda user: user.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegisterForm()

    context = {'form': form}

    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda user: user.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'adminapp/admin-product-read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = UserAdminCreateProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = UserAdminCreateProductForm()

    context = {'form': form}

    return render(request, 'adminapp/admin-product-create.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_products_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = UserAdminCreateProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = UserAdminCreateProductForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_products_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product, product.id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_products'))
