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
def eq(a, b):
    return a == b


@register.filter
def get(d, k):
    return d.get(k)


@register.filter
def prettify(val):
    return val.replace('%20', '+')
