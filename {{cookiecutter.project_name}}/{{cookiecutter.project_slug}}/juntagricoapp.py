from juntagrico.util import addons
import {{cookiecutter.project_slug}}


addons.config.register_user_menu('{{cookiecutter.project_initials}}/menu.html')
addons.config.register_version({{cookiecutter.project_slug}}.name, {{cookiecutter.project_slug}}.version)
