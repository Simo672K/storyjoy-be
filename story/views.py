from django.shortcuts import render
from .models import Author, Story, Chapter
from .utils import array_item_prev_next

# Create your views here.
def home(request):
  stories = Story.objects.all()
  context = {
    'stories': list(stories)
  }
  return render(request, 'index.html', context)

def story_details(request, pk):
  story= Story.objects.prefetch_related('chapter_set').select_related('author').get(pk= pk)
  context= {
    'story': story
  }
  return render(request, 'story-details.html', context)

def story_chapter(request, pk, slug):
  story = Story.objects.prefetch_related('chapter_set').get(pk= pk) 
  chapter = Chapter.objects.select_related('story').get(slug= slug)
  
  chapters = list(story.chapter_set.all())
  result = list(filter(lambda elm: elm.slug == slug, chapters))
  navigation = array_item_prev_next(chapters, result[0])

  context={
    'story': story,
    'chapter': chapter,
    'navigation': navigation,
  }
  return render(request, 'story-chapter.html', context)