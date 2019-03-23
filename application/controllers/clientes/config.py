import web
from web import form
import application.models.model_clientes

render = web.template.render('application/views/clientes/', base='master')
model = application.models.model_clientes

vemail = form.regexp(r".*@.*", "Must be a valid email address")
'''
Here we define the form fields for use in all the views
'''
form_clientes= form.Form(
            form.Hidden('id_cliente',description="", value="0", class_="form-control", required=True),
            form.Textbox('nombre',description="nombre", class_="form-control", required=True),
            form.Textbox('apellido paterno',description="apellido_paterno", class_="form-control", required=True),
            form.Textbox('apellido materno',description="apellido materno", class_="form-control", required=True),
            form.Textbox('telefono',description="telefono", class_="form-control", required=True),
            form.Textbox('email', vemail, description="Email", class_="form-control", required=True),
        )
        