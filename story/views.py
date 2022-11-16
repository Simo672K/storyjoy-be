from django.shortcuts import render
from .models import Author, Story, Chapter

# Create your views here.
def home(request):
  stories = Story.objects.all()
  context = {
    'stories': list(stories)
  }
  return render(request, 'index.html', context)

def story_details(request, pk):
  story= Story.objects.get(pk= pk).prefetch_related('chapter_set')
  context= {
    'story': list(story)
  }

  return render(request, 'story-details.html', context)