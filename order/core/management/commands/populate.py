from typing import Any, Optional

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from order.core.models import Client, Product


class Command(BaseCommand):
    help = "Populate database with predefined datas"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            self.__populate_client()
            self.__populate_product()

            self.stdout.write(self.style.SUCCESS("Successfully populated"))
        except OperationalError as error:
            migration_fault = "no such table"
            if migration_fault in str(error):
                self.stdout.write(
                    self.style.ERROR("Please, run migration before populate database.")
                )

    def __populate_client(self):
        for client in self.CLIENTS:
            Client.objects.get_or_create(**client)

    def __populate_product(self):
        for product in self.PRODUCTS:
            Product.objects.get_or_create(**product)
