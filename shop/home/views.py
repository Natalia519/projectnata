from django.shortcuts import get_object_or_404, render
from django.views import generic

# from django.contrib.auth.decorators import login_required, permission_required
# from django.http import HttpResponsePermanentRedirect


# @login_required()
def index(request):
    itemsCount = request.session.get("itemsCount", 0)
    cart_id = request.session.get("cart_id", 0)
    if request.user.is_authenticated:
        return render(request, 'index.html', {'itemsCount': itemsCount, 'cartId': cart_id})
    else:
    #     return HttpResponsePermanentRedirect("/accounts/login/")
        return render(request, 'index.html', {'itemsCount': itemsCount, 'cartId': cart_id})

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return ""


class ContactsView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ""
