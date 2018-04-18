from django.shortcuts import render, redirect
# from django.http import HttpResponse
# Create your views here.
from .forms import CommentForm
from .models import Comment

def index(request):
    comments = Comment.objects.order_by('-date')
    context = {'comments' : comments}
    return render(request, 'hw/index.html', context = context)

def sign(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],
                                comment = request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    context = {'form' : form}
    return render(request, 'hw/sign.html', context = context)
