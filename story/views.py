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
  story= Story.objects.prefetch_related('chapter_set').get(pk= pk)
  context= {
    'story': story
  }
  return render(request, 'story-details.html', context)

def story_chapter(request, pk, slug):
  chapter = Chapter.objects.get(slug= slug)
  context={
    'chapter': chapter
  }
  return render(request, 'story-chapter.html', context)