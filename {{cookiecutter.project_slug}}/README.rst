{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/kupfer_plugin_{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/kupfer_plugin_{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/kupfer_plugin_{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/kupfer_plugin_{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/kupfer_plugin_{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://kupfer_plugin_{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}



{{ cookiecutter.project_short_description }}

Require Kupfer https://github.com/kupferlauncher/kupfer/

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

Features
--------

* TODO

Install
-------

pip install kupfer_plugin_{{ cookiecutter.project_slug }}

Or copy {{ cookiecutter.project_slug }}.py to ~/.local/share/kupfer/plugins/

Credits
-------

This package was created with Cookiecutter_ and the `cookiecutter-kupfer-plugin-package`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-kupfer-plugin-package`: https://github.com/hugosenari/cookiecutter-kupfer-plugin-package

