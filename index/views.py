from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import NewsCategory, News
from  .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User





# Create your views here.
def home_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all()

    context = {'categories': categories, 'news': news}

    return render(request, 'home.html', context)


def news_home(request):
    return render(request, 'news/index.html')


class Register(View):
    template_name = 'registration/register.html'

    # Выдача формы
    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)


    # Получение инфы с формы
    def post(self, request):
        form = RegForm(request.POST)

        # Если данные корректны
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            # Создаем объект класса User
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            print(user)
            user.save()

            # Авторизуем пользователя
            login(request, user)
            return redirect('/')
        # Если данные некорректны
        context = {'form': RegForm, 'message': 'Пароль или почта неверны!'}
        return render(request, self.template_name, context)

def logout_view(request):
    logout(request)
    return redirect('/')



@login_required
def toggle_favorite(request, news_id):
    news = get_object_or_404(News, id=news_id)
    user = request.user

    if user in news.favorites.all():
        news.favorites.remove(user)
    else:
        news.favorites.add(user)

    return redirect('news_detail', news_id=news_id)  # redirect на страницу новости

@login_required
def favorite_news(request):
    user = request.user
    favorite_news = user.favorite_news.all()
    return render(request, 'news/favorite_news.html', {'favorite_news': favorite_news})
