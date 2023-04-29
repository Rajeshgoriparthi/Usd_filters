from django import template

register=template.Library()

@register.filter(name='swapping')
def swap(value):
    return value.swapcase()

@register.filter
def upper(value):
    return value.upper()

@register.filter()
def lower(value):
    return value.lower()

@register.filter()
def count(value,arg):
    c=0
    for a in range(len(value)):
        if arg==value[a:a+len(arg)]:
            c+=1
    return c

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')

# register.filter('swapping',swap)
# register.filter('upper',upper)
# register.filter('lower',lower)
# register.filter('count',count)