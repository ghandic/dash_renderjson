# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashRenderjson(Component):
    """A DashRenderjson component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- data (dict; optional): The value displayed in the input.
- max_depth (number; default 0): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- theme (dict; default {
        scheme: 'monokai',
        author: 'wimer hazenberg (http://www.monokai.nl)',
        base00: '#272822',
        base01: '#383830',
        base02: '#49483e',
        base03: '#75715e',
        base04: '#a59f85',
        base05: '#f8f8f2',
        base06: '#f5f4f1',
        base07: '#f9f8f5',
        base08: '#f92672',
        base09: '#fd971f',
        base0A: '#f4bf75',
        base0B: '#a6e22e',
        base0C: '#a1efe4',
        base0D: '#66d9ef',
        base0E: '#ae81ff',
        base0F: '#cc6633'
    })
- invert_theme (boolean; default False)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, max_depth=Component.UNDEFINED, theme=Component.UNDEFINED, invert_theme=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'max_depth', 'theme', 'invert_theme']
        self._type = 'DashRenderjson'
        self._namespace = 'dash_renderjson'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'max_depth', 'theme', 'invert_theme']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashRenderjson, self).__init__(**args)
