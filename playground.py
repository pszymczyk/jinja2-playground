import os
import jinja2

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

context = {
    'firstname': 'John',
    'lastname': 'Doe'
}

result = render('/home/pszymczyk/dev/repo/jinja-playground/template.conf', context)

print(result)
