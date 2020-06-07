from django import template
register = template.Library()


#@register.filter(name= 't_n')
def truncate_n(value):
	#result = vlaue[0:n]
	result = 'sachin'

	return result


register.filter('t_n', truncate_n)

#example of templae tag

'''@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - date.today()

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
            ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days


        {% load app_filters %}
{% for todo in todos %}
    ...
    <div class='due_date'>
        <b>Due:</b> {{ todo.due_date|get_due_date_string }}
    </div>
    ...
{% endfor %}

'''