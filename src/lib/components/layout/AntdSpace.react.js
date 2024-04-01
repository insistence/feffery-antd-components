// react核心
import PropTypes from 'prop-types';
// antd核心
import { Space, Divider } from 'antd';
// 辅助库
import { isString } from 'lodash';
import { parseChildrenToArray } from '../utils';
// 自定义hooks
import useCss from '../../hooks/useCss';

/**
 * 排列组件AntdSpace
 */
const AntdSpace = (props) => {
    let {
        id,
        children,
        className,
        style,
        key,
        align,
        direction,
        size,
        customSplit,
        wrap,
        addSplitLine,
        styles,
        classNames,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children)

    if (addSplitLine) {
        if (direction === 'horizontal') {
            return (
                <Space id={id}
                    className={
                        isString(className) ?
                            className :
                            (className ? useCss(className) : undefined)
                    }
                    style={style}
                    styles={styles}
                    classNames={classNames}
                    key={key}
                    align={align}
                    direction={direction}
                    size={size}
                    split={<Divider type="vertical" />}
                    wrap={wrap}
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    }>
                    {children}
                </Space>
            );
        }
        return (
            <Space id={id}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                styles={styles}
                classNames={classNames}
                key={key}
                align={align}
                direction={direction}
                size={size}
                split={<Divider />}
                wrap={wrap}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }>
                {children}
            </Space>
        );
    }

    return (
        <Space id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            styles={styles}
            classNames={classNames}
            key={key}
            align={align}
            direction={direction}
            size={size}
            split={customSplit}
            wrap={wrap}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {children}
        </Space>
    );
}

AntdSpace.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

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
     * 细分控制子元素css样式
     */
    styles: PropTypes.exact({
        /**
         * 控制子项容器元素css样式
         */
        item: PropTypes.object
    }),

    /**
     * 细分控制子元素css类
     */
    classNames: PropTypes.exact({
        /**
         * 控制子项容器元素css类
         */
        item: PropTypes.string
    }),

    /**
     * 对齐方式，可选项有`'start'`、`'end'`、`'center'`、`'baseline'`
     */
    align: PropTypes.oneOf(['start', 'end', 'center', 'baseline']),

    /**
     * 排列方向，可选项有`'vertical'`、`'horizontal'`
     * 默认值：`'horizontal'`
     */
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 子元素间隔大小，可选项有`'small'`、`'middle'`、`'large'`，或直接设置数值型代表像素间隔
     * 默认值：`'small'`
     */
    size: PropTypes.oneOfType([
        PropTypes.oneOf(['small', 'middle', 'large']),
        PropTypes.number
    ]),

    /**
     * 是否添加分隔线
     * 默认值：`false`
     */
    addSplitLine: PropTypes.bool,

    /**
     * 自定义分隔线元素
     */
    customSplit: PropTypes.node,

    /**
     * 子元素是否自动换行，仅`direction='horizontal'`时有效
     * 默认值：`false`
     */
    wrap: PropTypes.bool,

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
AntdSpace.defaultProps = {
    direction: 'horizontal',
    size: 'small',
    addSplitLine: false,
    wrap: false
}

export default AntdSpace;