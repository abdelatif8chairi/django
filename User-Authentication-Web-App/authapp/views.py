from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import UserRegistration, UserEditForm, GraphicForm
from .models import GraphiCards


# Create your views here.

@login_required
def dashboard(request):
    # Getting all the stuff from database
    query_results = GraphiCards.objects.all()
    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results}
    return render(request, 'authapp/dashboard.html', context=context)

@permission_required('authapp.add_item', raise_exception=True)
@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = GraphicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = GraphicForm()
    return render(request, 'authapp/model_form_upload.html', {
        'form': form
    })

@permission_required('authapp.update_item', raise_exception=True)
@login_required
def updateitem(request, pk):
    graphiCards = GraphiCards.objects.get(id=pk)
    print(graphiCards)
    form = GraphicForm(instance=graphiCards)

    if request.method == 'POST':
        form = GraphicForm(request.POST, instance=graphiCards)
        if form.is_valid():
            form.save()
            redirect('authapp/dashboard.html')

    context = {'orders': form}
    print(form)
    return render(request, 'authapp/update_item.html', context)

@permission_required('authapp.delete_item', raise_exception=True)
@login_required
def delete_item(request, pk):
    order = GraphiCards.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'authapp/delete_item.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/model_form_upload.html', context=context)
