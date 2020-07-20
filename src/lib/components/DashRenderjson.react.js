import React, { Component } from 'react';
import PropTypes from 'prop-types';

import JSONTree from 'react-json-tree'

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashRenderjson extends Component {
    render() {
        const { id, data, max_depth, theme, invert_theme } = this.props;

        return (
            <div id={id}>
                {data ? <JSONTree
                    data={data}
                    theme={theme}
                    invertTheme={invert_theme}
                    shouldExpandNode={(_keyName, _data, level) => (max_depth === -1) ? true : (level < max_depth)}
                /> : ''}
            </div>
        );
    }
}

DashRenderjson.defaultProps = {
    max_depth: 0, theme: {
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
    }, invert_theme: false
};

DashRenderjson.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    // label: PropTypes.string.isRequired,

    /**
     * The value displayed in the input.
     */
    data: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    // setProps: PropTypes.func,

    max_depth: PropTypes.number,

    theme: PropTypes.object,

    invert_theme: PropTypes.bool,
};
