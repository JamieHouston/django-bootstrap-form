from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(element, icon=None):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field.html")
        context_dic = {'field': element}
        if icon:
            context_dic["icon"] = icon
        context = Context(context_dic)
    else:
        template = get_template("bootstrapform/form.html")
        context = Context({'form': element})
        
    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"

@register.filter
def is_file(field): 
    return field.field.widget.__class__.__name__.lower() == "fileinput"