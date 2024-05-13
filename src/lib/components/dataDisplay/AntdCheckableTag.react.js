import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyAntdCheckableTag = React.lazy(() => import(/* webpackChunkName: "data_display" */ '../../fragments/dataDisplay/AntdCheckableTag.react'));

/**
 * 可选择标签AntdCheckableTag
 */
const AntdCheckableTag = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdCheckableTag {...props} />
        </Suspense>
    );
}

AntdCheckableTag.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 组件型，标签内容
     */
    content: PropTypes.node,

    /**
     * 组件型，选择状态下的标签内容
     */
    checkedContent: PropTypes.node,

    /**
     * 组件型，未选择状态下的标签内容
     */
    unCheckedContent: PropTypes.node,

    /**
     * 监听或设置当前标签的选择状态
     * 默认值：`false`
     */
    checked: PropTypes.bool,

    /**
     * `data-*`格式属性通配
     */
    'data-*': PropTypes.string,

    /**
     * `aria-*`格式属性通配
     */
    'aria-*': PropTypes.string,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
AntdCheckableTag.defaultProps = {
    checked: false
}

export default AntdCheckableTag;

export const propTypes = AntdCheckableTag.propTypes;
export const defaultProps = AntdCheckableTag.defaultProps;