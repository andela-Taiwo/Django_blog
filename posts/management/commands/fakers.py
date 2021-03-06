from django.contrib.auth.models import User
import factory.django
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    # import pdb;pdb.set_trace()
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    username = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.Faker('password')
