from tqdm import tqdm
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.repositories import get_concrete_models

Author, Post = get_concrete_models()


class Command(BaseCommand):
    help = 'Generate fake authors for performance testing'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of authors to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        authors = []

        batch_size = 1000

        for _ in tqdm(range(total)):
            name = fake.name()
            biography = fake.text()
            date_of_birth = fake.date_of_birth(minimum_age=20, maximum_age=90)
            authors.append(Author(name=name, biography=biography, date_of_birth=date_of_birth))

            if len(authors) >= batch_size:
                Author.objects.insert(authors)
                authors = []

        # Insert any remaining authors
        if authors:
            Author.objects.insert(authors)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} authors'))
