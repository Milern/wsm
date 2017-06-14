from django.shortcuts import render
from .models import Music_Info_Detail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
#def search(request):
#    return render(request,'music/search.html')

def search_results(request):
    latest_search_result_list = Music_Info_Detail.objects.filter(music_title=request.POST['search_text'])
    #latest_search_result_list_2 = Music_Info_Detail.objects.order_by('music_cloud_id')[:5]
    context = {'latest_search_result_list':latest_search_result_list}
    return render(request, 'music/search_list.html',context)

def song_id(request, song_num):
    song = Music_Info_Detail.objects.get(music_local_id=song_num)
    return render(request,'music/song_detail.html',{'song':song})
