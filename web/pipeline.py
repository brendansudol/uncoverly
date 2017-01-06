def get_avatar(backend, details, response, uid, user, *args, **kwargs):
    social_user = kwargs.get('social') or \
        backend.strategy.storage.user.get_social_auth(backend.name, uid)

    if social_user:
        if backend.name == 'facebook':
            url = 'http://graph.facebook.com/{}/picture?type=large'.format(uid)
        if backend.name == 'twitter':
            url = response.get('profile_image_url', '').replace('_normal', '')

        social_user.extra_data['avatar'] = url
        social_user.save()
