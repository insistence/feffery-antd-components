# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdMentions(Component):
    """An AntdMentions component.


Keyword arguments:

- id (string; optional)

- autoFocus (boolean; default False)

- autoSize (dict; default False)

    `autoSize` is a boolean | dict with keys:

    - maxRows (number; optional)

    - minRows (number; optional)

- batchPropsNames (list of strings; optional)

- batchPropsValues (dict; optional)

- bordered (boolean; default True):
    设置是否渲染边框，设置为True时等价于variant='outlined'  默认：True.

- className (string | dict; optional)

- defaultValue (string; optional)

- disabled (boolean; default False)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- options (list of dicts; required)

    `options` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional)

    - value (string; optional)

- placement (a value equal to: 'top', 'bottom'; default 'bottom')

- popupClassName (string; optional):
    设置弹框菜单css类名.

- popupContainer (a value equal to: 'parent', 'body'; optional)

- prefix (string; default '@')

- selectedOptions (list of strings; optional)

- status (a value equal to: 'error', 'warning'; optional)

- style (dict; optional)

- value (string; optional)

- variant (a value equal to: 'outlined', 'borderless', 'filled'; optional):
    设置形态变体类型，可选的有'outlined'、'borderless'、'filled'
    其中'outlined'等价于bordered=True，优先级高于bordered."""
    _children_props = ['options[].label']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdMentions'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, popupClassName=Component.UNDEFINED, key=Component.UNDEFINED, autoSize=Component.UNDEFINED, prefix=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, options=Component.REQUIRED, selectedOptions=Component.UNDEFINED, disabled=Component.UNDEFINED, placement=Component.UNDEFINED, bordered=Component.UNDEFINED, variant=Component.UNDEFINED, status=Component.UNDEFINED, autoFocus=Component.UNDEFINED, popupContainer=Component.UNDEFINED, batchPropsNames=Component.UNDEFINED, batchPropsValues=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoFocus', 'autoSize', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'placement', 'popupClassName', 'popupContainer', 'prefix', 'selectedOptions', 'status', 'style', 'value', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoFocus', 'autoSize', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'placement', 'popupClassName', 'popupContainer', 'prefix', 'selectedOptions', 'status', 'style', 'value', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdMentions, self).__init__(**args)
