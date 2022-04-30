from django.http import JsonResponse, HttpResponse
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
        remote_addr = request.META.get('REMOTE_ADDR')
        channel, created = Channel.objects.get_or_create(id=channel_id)
        ClipBoardContent.objects.create(
            content=content,
            channel=channel,
            publish_ip=remote_addr,
        )
        return redirect(to=reverse('retrieve_or_delete_content', kwargs={'pk': channel_id}))


def retrieve_or_delete_content(request, pk):
    if request.method == 'GET':
        channel = Channel.objects.filter(pk=pk).first()
        if channel:
            contents = channel.clipboardcontent_set.all().order_by('-create_at')
        else:
            contents = []
        return render(request, 'detail.html', context={'channel': channel, 'contents': contents})
    elif request.method == 'DELETE':
        ClipBoardContent.objects.get(pk=pk).delete()
        return JsonResponse({'code': 1000, 'message': 'success'})


def clear_all_content(request, pk):
    ClipBoardContent.objects.filter(channel_id=pk).delete()
    return redirect(reverse('retrieve_or_delete_content', kwargs={'pk': pk}))


def retrieve_single_content(request, pk):
    content = ClipBoardContent.objects.get(pk=pk).content
    return HttpResponse(content + '\n')
