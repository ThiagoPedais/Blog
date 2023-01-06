from django import template


register = template.Library()

@register.filter(name="plural_comments")
def plural_comments(num_comments):
    try:
        num_comments = int(num_comments)

        if num_comments == 0:
            return f"Nenhum comentário"
        elif num_comments == 1:
            return f"{num_comments} comentário"
        else:
            f"{num_comments} comentários"
    except:
        return f"{num_comments} comentário(s)"