from django.db import models

class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable

class AutoSlug():
    def unique_slug(item,slug_source,slug_field):
      """Ensures a unique slug field by appending an integer counter to duplicate slugs.
      
      The item's slug field is first prepopulated by slugify-ing the source field. If that value already exists, a counter is appended to the slug, and the counter incremented upward until the value is unique.
      
      For instance, if you save an object titled Daily Roundup, and the slug daily-roundup is already taken, this function will try daily-roundup-2, daily-roundup-3, daily-roundup-4, etc, until a unique value is found.
      
      Call from within a model's custom save() method like so:
      unique_slug(item, slug_source='field1', slug_field='field2')
      where the value of field slug_source will be used to prepopulate the value of slug_field.
      """
      if not getattr(item, slug_field): # if it's already got a slug, do nothing.
          from django.template.defaultfilters import slugify
          slug = slugify(getattr(item,slug_source))
          itemModel = item.__class__
          # the following gets all existing slug values
          allSlugs = [sl.values()[0] for sl in itemModel.objects.values(slug_field)]
          if slug in allSlugs:
              import re
              counterFinder = re.compile(r'-\d+$')
              counter = 2
              slug = "%s-%i" % (slug, counter)
              while slug in allSlugs:
                  slug = re.sub(counterFinder,"-%i" % counter, slug)
                  counter += 1
          setattr(item,slug_field,slug)
    unique_slug = Callable(unique_slug)
        

