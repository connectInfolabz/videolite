
from django import template
from datetime import datetime

register = template.Library()

@register.filter('months_since')
def months_since(date_string):
    # Assuming date_string is in ISO 8601 format, like '2021-03-15T12:30:00Z'
    publish_date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    current_date = datetime.now()
    # Calculate the number of months between the dates
    months = (current_date.year - publish_date.year) * 12 + current_date.month - publish_date.month
    return months