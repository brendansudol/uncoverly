def favorites(request):
    def _fetch():
        if not request.user.is_authenticated():
            return []

        favorites = request.user.favorites \
            .values_list('product_id', flat=True)

        return favorites

    return {'favorites': _fetch()}
