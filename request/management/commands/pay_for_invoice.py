from django.core.management.base import BaseCommand, CommandError

from request.models import Invoice


class Command(BaseCommand):
    help = 'Change Invoice status from Unpaid to Paid-up'

    def add_arguments(self, parser):
        parser.add_argument('invoice_id', type=int)

    def handle(self, *args, **options):
        invoice_id = options['invoice_id']
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
        except Invoice.DoesNotExist:
            raise CommandError('Invoice "%s" does not exist' % invoice_id)

        invoice.status = Invoice.PAID_UP
        invoice.save()

        self.stdout.write(self.style.SUCCESS('The payment is successful for "%s"' % invoice))
    