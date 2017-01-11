from django import template


register = template.Library()


@register.simple_tag
def make_url(url, page, query=None):
    path = '{}?{}{}'.format(
        url,
        'q={}&'.format(query) if query else '',
        'page={}'.format(page)
    )
    return path


@register.filter
def get(d, k):
    return d.get(k)
