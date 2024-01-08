import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

            create_catalog = []
            create_product = []

            with open('data.json', 'r', encoding='utf-8') as file:
                 template = json.load(file)
                 for item in template:
                    if item["model"] == "catalog.category":
                        categories = {"name": item["fields"]["name"],
                                      "description": item["fields"]["description"]}
                        create_catalog.append(Category(**categories))
                    elif item["model"] == "catalog.product":
                        products = {"name": item["fields"]["name"],
                                      "description": item["fields"]["description"],
                                    "category": item["fields"]["category"],
                                      "price_for_one": item["fields"]["price_for_one"]}
                        create_product.append(Product(**products))

            # Category.objects.bulk_create(create_catalog)
            # Product.objects.bulk_create(create_product)

            print(create_catalog)
            print(create_product)