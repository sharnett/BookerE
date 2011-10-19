from django import template
register = template.Library()


@register.inclusion_tag('books.djhtml')
def renderBooksForUser(user):
    """
    render books for user
    in turn calls the render_person method for members
    """
    return dict(user = user)
