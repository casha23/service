from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create master user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()

    def add_arguments(self, parser):
        parser.add_argument('phone_number', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        try:
            # Phone number validate
            try:
                self.UserModel._meta.get_field('phone_number').clean(options['phone_number'], None)
            except Exception as e:
                raise CommandError(e)
    
            user_data = {
                'phone_number': options['phone_number'],
                'email': '',
                'password': options['password']
            }
            user = self.UserModel._default_manager.create_user(**user_data)
        except Exception as e:
            raise CommandError(e)

        user.is_master = True
        user.save()

        self.stdout.write(self.style.SUCCESS('Successfully master user created "%s"' % user))
    