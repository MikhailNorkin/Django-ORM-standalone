import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    posts = Passcard.objects.all()
    print(posts)
    print()
  
    print('owner_name: ' + str(posts[0]))
    print('passcode: ' + str(posts[0].created_at))
    print('created_at: ' + str(posts[0].passcode))
    print('is_active: ' + str(posts[0].owner_name))
    print()

    list_active = []
    for post in posts:
      if post.is_active == True:
        list_active.append(post.owner_name)
    ## print(list_active)
    print(len(list_active))
    print()

    published_posts = Passcard.objects.filter(is_active=True)
    print(len(published_posts))
    print()

    
      
      