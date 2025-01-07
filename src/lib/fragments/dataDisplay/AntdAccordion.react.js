// react核心
import React, { useEffect, useContext } from 'react';
// antd核心
import { Collapse } from 'antd';
// 辅助库
import { isString, isUndefined } from 'lodash';
import { pickBy } from 'ramda';
// 自定义hooks
import useCss from '../../hooks/useCss';
// 上下文
import PropsContext from '../../contexts/PropsContext';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataDisplay/AntdAccordion.react';

const { Panel } = Collapse;

/**
 * 手风琴组件AntdAccordion
 */
const AntdAccordion = (props) => {
    let {
        id,
        className,
        style,
        key,
        items,
        accordion,
        activeKey,
        defaultActiveKey,
        bordered,
        size,
        collapsible,
        expandIconPosition,
        ghost,
        loading_state,
        setProps
    } = props;

    useEffect(() => {
        if (defaultActiveKey && !activeKey) {
            setProps({ activeKey: defaultActiveKey })
        }
    }, [])

    const context = useContext(PropsContext)

    return (
        <Collapse
            // 提取具有data-*或aria-*通配格式的属性
            {...pickBy((_, k) => k.startsWith('data-') || k.startsWith('aria-'), props)}
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            accordion={accordion}
            activeKey={activeKey}
            defaultActiveKey={defaultActiveKey}
            bordered={bordered}
            size={
                context && !isUndefined(context.componentSize) ?
                    context.componentSize :
                    size
            }
            collapsible={collapsible}
            expandIconPosition={expandIconPosition}
            ghost={ghost}
            onChange={(e) => setProps({ activeKey: e })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {
                items ? (
                    items.map(
                        item => (
                            <Panel
                                className={
                                    isString(item.className) ?
                                        item.className :
                                        (item.className ? useCss(item.className) : undefined)
                                }
                                style={item.style}
                                key={item.key}
                                collapsible={item.collapsible}
                                header={item.title}
                                extra={item.extra}
                                showArrow={item.showArrow}
                                forceRender={item.forceRender}>
                                {item.children}
                            </Panel>
                        )
                    )
                ) : null
            }
        </Collapse>
    );
}

export default AntdAccordion;

AntdAccordion.defaultProps = defaultProps;
AntdAccordion.propTypes = propTypes;