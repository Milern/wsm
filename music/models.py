from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Music_Info_Detail(models.Model):
      music_local_id = models.IntegerField(default=0,primary_key=True)
      music_cloud_id = models.IntegerField(default=0)
      music_title = models.CharField(max_length=100,default=' ')
      music_singer = models.CharField(max_length=100,default=' ')
      music_album = models.CharField(max_length=100,default=' ')
      lyric_path = models.CharField(max_length=200,default=' ',blank=True)
      music_path = models.CharField(max_length=200, default=' ',blank=True)
      album_cover_path = models.CharField(max_length=200, default=' ',blank=True)
      music_type_label = models.CharField(max_length=200,default=' ')
      play_time = models.IntegerField(default=0,blank=True)
      frame_num = models.IntegerField(default=0,blank=True)

      def __str__(self):
          return str(self.music_local_id) +" "+ self.music_title
