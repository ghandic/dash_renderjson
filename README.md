# Dash renderjson

Dash renderjson is a Dash component library, it makes use of [react-json-tree](https://github.com/reduxjs/redux-devtools/tree/master/packages/react-json-tree) from redux-devtools and allows you to render a simple dictionary object (currently basic types supported)

Get started with:

1. Install Dash and its dependencies: https://dash.plotly.com/installation
2. Run `pip install dash-renderjson`

## Useage

> Note: This demo useage makes use of `dash_daq` for the ToggleSwitch

```python
import dash_renderjson
import dash
import dash_daq as daq
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)


app.layout = html.Div([daq.ToggleSwitch(id="my-toggle-switch", value=False), html.Div(id="output")])


@app.callback(Output("output", "children"), [Input("my-toggle-switch", "value")])
def display_output(value):
    if value:
        data = {"a": 1, "b": [1, 2, 3, {"c": 4}]}
        theme = {
            "scheme": "monokai",
            "author": "wimer hazenberg (http://www.monokai.nl)",
            "base00": "#272822",
            "base01": "#383830",
            "base02": "#49483e",
            "base03": "#75715e",
            "base04": "#a59f85",
            "base05": "#f8f8f2",
            "base06": "#f5f4f1",
            "base07": "#f9f8f5",
            "base08": "#f92672",
            "base09": "#fd971f",
            "base0A": "#f4bf75",
            "base0B": "#a6e22e",
            "base0C": "#a1efe4",
            "base0D": "#66d9ef",
            "base0E": "#ae81ff",
            "base0F": "#cc6633",
        }
        return dash_renderjson.DashRenderjson(id="input", data=data, max_depth=-1, theme=theme, invert_theme=True)


if __name__ == "__main__":
    app.run_server(debug=True)

```

## Configuration options

- `id` - Required, the id of the JSONRenderer element to create
- `data` - Required, the dictionary you want to display
- `max_depth` - (-1) shows full JSON, 0 hides all but root, 1 shows one max depth, etc
- `theme` - A theme dictionary, example given above
- `invert_theme` - Whether to invert the colors of the supplied/default theme

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

### Install dependencies

If you have selected install_dependencies during the prompt, you can skip this part.

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.
    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```
    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Write your component code in `src/lib/components/DashRenderjson.react.js`.

- The demo app is in `src/demo` and you will import your example component code into your demo app.
- Test your code in a Python environment:
    1. Build your code
        ```
        $ npm run build
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```
- Write tests for your component.
    - A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    - Run the tests with `$ pytest tests`.
    - The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Add custom styles to your component by putting your custom CSS files into your distribution folder (`dash_renderjson`).
    - Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    - Make sure the stylesheets are added to the `_css_dist` dict in `dash_renderjson/__init__.py` so dash will serve them automatically when the component suite is requested.
- [Review your code](./review_checklist.md)

### Create a production build and publish:

1. Build your code:
    ```
    $ npm run build
    ```
2. Create a Python tarball
    ```
    $ python setup.py sdist
    ```
    This distribution tarball will get generated in the `dist/` folder

3. Test your tarball by copying it into a new environment and installing it locally:
    ```
    $ pip install dash_renderjson-0.0.1.tar.gz
    ```

4. If it works, then you can publish the component to NPM and PyPI:
    1. Publish on PyPI
        ```
        $ twine upload dist/*
        ```
    2. Cleanup the dist folder (optional)
        ```
        $ rm -rf dist
        ```
    3. Publish on NPM (Optional if chosen False in `publish_on_npm`)
        ```
        $ npm publish
        ```
        _Publishing your component to NPM will make the JavaScript bundles available on the unpkg CDN. By default, Dash serves the component library's CSS and JS locally, but if you choose to publish the package to NPM you can set `serve_locally` to `False` and you may see faster load times._

5. Share your component with the community! https://community.plotly.com/c/dash
    1. Publish this repository to GitHub
    2. Tag your GitHub repository with the plotly-dash tag so that it appears here: https://github.com/topics/plotly-dash
    3. Create a post in the Dash community forum: https://community.plotly.com/c/dash
