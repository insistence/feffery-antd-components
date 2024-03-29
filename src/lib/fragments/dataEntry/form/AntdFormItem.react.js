import React, { useMemo } from 'react';
import { Form } from 'antd';
import { isString } from 'lodash';
import useCss from '../../../hooks/useCss';
import { propTypes, defaultProps } from '../../../components/dataEntry/form/AntdFormItem.react';

const { Item } = Form;

// 定义表单项组件AntdFormItem，api参数参考https://ant.design/components/form-cn/
const AntdFormItem = (props) => {
    // 取得必要属性或参数
    let {
        id,
        children,
        className,
        style,
        key,
        name,
        labelCol,
        colon,
        wrapperCol,
        label,
        labelAlign,
        tooltip,
        extra,
        help,
        hidden,
        required,
        rules,
        validateStatus,
        hasFeedback,
        setProps,
        loading_state
    } = props;

    if (rules) {
        rules.forEach(item => {
            // 处理表单项值为false时使用validateFields但校验规则不触发的问题
            item.transform = (inputValue) => {
                if (inputValue === false) {
                    return null;
                }
                return inputValue;
            };
            item.pattern = item.pattern ? new RegExp(item.pattern) : item.pattern;
        });
    }

    const validateTrigger = useMemo(() => {
        return rules ? rules.map((rule) => {
            return rule.validateTrigger ? rule.validateTrigger : 'onChange'
        }) : []
    })

    return (
        <Item id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            labelCol={labelCol}
            colon={colon}
            wrapperCol={wrapperCol}
            label={label}
            labelAlign={labelAlign}
            tooltip={tooltip}
            extra={extra}
            help={help}
            hasFeedback={hasFeedback}
            hidden={hidden}
            required={required || (rules && rules.length > 0 && rules.some(item => item.required)) ? true : false}
            rules={rules}
            validateStatus={validateStatus}
            validateTrigger={validateTrigger}
            name={name}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {children}
        </Item>
    );
}

export default React.memo(AntdFormItem);

AntdFormItem.defaultProps = defaultProps;
AntdFormItem.propTypes = propTypes;