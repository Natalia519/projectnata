from django.views import generic
from .models import Contacts


class IndexView(generic.ListView):
    template_name = 'contacts.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Contacts.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        itemsCount = self.request.session.get("itemsCount", None)
        if cart_id == None:
            context['itemsCount'] = 0
            context['cart_id'] = 0
        else:
            context['itemsCount'] = itemsCount
            context['cart_id'] = cart_id
        return context
