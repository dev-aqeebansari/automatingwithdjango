from django.shortcuts import render
from dal import autocomplete

from .utils import scrape_stock_data
from.models import Stock
from .forms import StockForm
# Create your views here.

def stocks(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_id = request.POST.get('stock')
            # fetch the stock first and symbol
            stock = Stock.objects.get(pk=stock_id)
            symbol= stock.symbol
            exchange = stock.exchange
            print(exchange)
            print("symbol ==>  ", symbol)
            stock_response = scrape_stock_data(symbol, exchange)
            print(stock_response)
        else:
            print('form is not valid')
    else:
        form = StockForm()
        context = {
            'form' : form,
        }
        return render(request, 'stockanalysis/stocks.html', context)

class StockAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Stock.objects.all()

        if self.q:
            print('entered_keyword=> ', self.q)
            qs = qs.filter(name__istartswith=self.q)

        return qs