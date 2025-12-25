import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = "Load bank & branch data from CSV (duplicate safe) with progress"

    def handle(self, *args, **kwargs):
        file_path = "data/bank_branches.csv"

        #  Clear Clear old data
        Branch.objects.all().delete()
        Bank.objects.all().delete()

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            total_rows = len(rows)

            for idx, row in enumerate(rows, start=1):
                # Bank (duplicate-safe)
                bank, created = Bank.objects.get_or_create(
                    bank_id=int(row["bank_id"]),
                    defaults={"name": row["bank_name"]}
                )

              
                Branch.objects.update_or_create(
                    ifsc=row["ifsc"],
                    defaults={
                        "bank": bank,
                        "branch": row["branch"],
                        "address": row["address"],
                        "city": row["city"],
                        "district": row["district"],
                        "state": row["state"]
                    }
                )

                # Checking the Progress of loading data
                if idx % 1000 == 0 or idx == total_rows:
                    self.stdout.write(self.style.SUCCESS(f"{idx}/{total_rows} rows loaded"))

        self.stdout.write(self.style.SUCCESS("CSV loaded successfully!"))
