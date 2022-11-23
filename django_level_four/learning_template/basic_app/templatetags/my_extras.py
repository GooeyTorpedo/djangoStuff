from django import template

register = template.Library()


# def customF(value, arg):
#     """
#     # this cuts out all values of "arg" from the strin!
#     """
#     return value.replace(arg, '')


#  register.filter('customF', customF)
# instead of calling the above , we use function decorator


@register.filter(name='customF')
def customF(value, arg):
    """
    # this cuts out all values of "arg" from the strin!
    """
    return value.replace(arg, '')
