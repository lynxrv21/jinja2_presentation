import os
from jinja2 import Environment, FileSystemLoader

PATH = '.'
TEMPLATE_ENV = Environment(autoescape=False,
                           loader=FileSystemLoader(os.path.join(PATH, 'templates')),
                           trim_blocks=False)

# output_file = 'results/output.html'
output_file = 'results/output_config.cfg'

file_context = {
    'my_title' : 'The Title',
    'my_string' : 'smart quote',
    'my_list' : [1, 2, 'kitten', 12]
}

config_file_context = {
    'log_root_level' : 'info',
    'log_output' : 'logfile',
    'log_filehandler_level' : 'error'
}

def render_template(template_filename, context):
    return TEMPLATE_ENV.get_template(template_filename).render(context)

def create_file(fname, context):
    with open(fname, 'w') as f:
        # html = render_template('template.html', context)
        html = render_template('template.cfg', context)
        f.write(html)

create_file(output_file, config_file_context)