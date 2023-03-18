from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone
from user_paste.models import User, Post
import datetime
import string

class Command(BaseCommand):
    help = 'Generates fake data for a local sqlite database'

    def add_arguments(self, parser):
        parser.add_argument('--num_users', type=int, required=True)
        parser.add_argument('--num_user_posts', type=int, required=True)

    def handle(self, *args, **options):
        created_date = timezone.now() - datetime.timedelta(weeks=100)
        for i in range(options['num_users']):
            user_name = get_random_string(20, string.ascii_letters + string.digits)
            user = User.objects.create(user_name=user_name)
            for i in range(options['num_user_posts']):
                created_date += datetime.timedelta(days=1)
                post_content = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                                  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                                  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                                  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
                Post(post_title = user.user_name + f'post{i}',
                        post_author = user,
                        post_content = post_content,
                        post_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing',
                        post_category = 'Plain Text',
                        post_type = 'Notes',
                        post_created_date = created_date).save()
