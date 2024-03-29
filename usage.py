import dash
from dash import html
import feffery_antd_components as fac


app = dash.Dash(__name__)

app.layout = html.Div(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(
                    id='test-field1',
                    placeholder='please input your phone number'
                ),
                label='AntdInput',
                name='AntdInput',
                rules=[
                    {
                        'required': True,
                        'message': 'invalid phone number',
                        'validateTrigger': 'onBlur',
                        'pattern': '^(?:(?:\+|00)86)?1[3-9]\d{9}$'
                    },
                ]
            ),
        ],
        id='demo-form',
        labelCol={
            'span': 3
        },
    ),
    style={
        'padding': '50px 100px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
