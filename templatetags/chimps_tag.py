from django import template
from request.models import Request

register = template.Library()

def strong_links(links):
    screen_name, user_id = (links['screen_name'], links['user_id'])
    for idx in range(len(links['strong_links'])):
        strong_link = links['strong_links'][idx]
        if strong_link is None:
            continue
        # get screen_name for id (id is link[0], link strength is link[1])