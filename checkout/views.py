from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K0q2FHQRbsxYaM5tB1JhVRUI2ihH1Qi3jZvdpXxoHtpnPjaPu04IkYLho5eVXgxMZApMBQw6w22lYzp8No5hlbD00lvWFC6Nw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)