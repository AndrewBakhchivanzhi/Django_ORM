import psycopg2
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        with psycopg2.connect(host='localhost', database='django_orm',
                              user='postgres', password='krot123.A') as conn:

            with conn.cursor() as cur:
                cur.execute("DELETE FROM catalog_product")
                cur.execute("DELETE FROM catalog_category")

        conn.close()




