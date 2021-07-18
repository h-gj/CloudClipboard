from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from main.models import ClipBoardContent, Channel


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        content = request.POST.get('content')
        channel_id = request.POST.get('channel_id')

        channel, created = Channel.objects.get_or_create(id=channel_id)

        ClipBoardContent.objects.create(
            content=content,
            channel=channel,
            publish_ip='127.0.0.1'
        )
        return redirect(to=reverse('retrieve_or_delete_content', kwargs={'pk': channel_id}))


def retrieve_or_delete_content(request, pk):
    if request.method == 'GET':
        print('pk', pk)
        channel = Channel.objects.get(pk=pk)
        contents = channel.clipboardcontent_set.all().order_by('-create_at')
        return render(request, 'detail.html', context={'channel': channel, 'contents': contents})
    elif request.method == 'DELETE':
        ClipBoardContent.objects.get(pk=pk).delete()
        return JsonResponse({'code': 1000, 'message': 'success'})
