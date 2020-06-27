from django.shortcuts import get_object_or_404, render
from django.views import generic

# from django.contrib.auth.decorators import login_required, permission_required
# from django.http import HttpResponsePermanentRedirect


# @login_required()
def index(request):
    # if request.user.is_authenticated:
    #     return render(request, 'index.html', {})
    # else:
    #     return HttpResponsePermanentRedirect("/accounts/login/")
    return render(request, 'index.html', {})

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
