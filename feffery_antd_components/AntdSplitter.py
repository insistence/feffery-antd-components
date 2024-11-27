# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSplitter(Component):
    """An AntdSplitter component.
分隔面板组件AntdSplitter

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    布局方向，可选项有`'horizontal'`、`'vertical'`  默认值：`'horizontal'`.

- items (list of dicts; required):
    配置分隔面板子项.

    `items` is a list of dicts with keys:

    - key (string; optional):
        当前子项唯一识别`key`.

    - children (a list of or a singular dash component, string or number; optional):
        组件型，内嵌元素.

    - style (dict; optional):
        当前子项`css`样式.

    - className (string; optional):
        当前子项`css`类名.

    - defaultSize (number

      Or string; optional):
        初始面板尺寸，支持数字`px`或者文字`'百分比%'`类型.

    - size (number | string; optional):
        面板尺寸，支持数字`px`或者文字`'百分比%'`类型.

    - min (number | string; optional):
        最小尺寸，支持数字`px`或者文字`'百分比%'`类型.

    - max (number | string; optional):
        最大尺寸，支持数字`px`或者文字`'百分比%'`类型.

    - collapsible (dict; optional):
        是否可折叠  默认值：`False`.

        `collapsible` is a boolean | dict with keys:

        - start (boolean; optional)

        - end (boolean; optional)

    - resizable (boolean; optional):
        是否开启拖拽伸缩  默认值：`True`.

- data-* (string; optional):
    `data-*`格式属性通配.

- aria-* (string; optional):
    `aria-*`格式属性通配.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['items[].children']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdSplitter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, layout=Component.UNDEFINED, items=Component.REQUIRED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'layout', 'items', 'data-*', 'aria-*', 'loading_state']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'key', 'style', 'className', 'layout', 'items', 'data-*', 'aria-*', 'loading_state']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdSplitter, self).__init__(**args)