from django.shortcuts import render


def view_wish_list(request):
    """ A view that renders the wish list contents page """

    return render(request, 'wish_list/wish_list.html')
