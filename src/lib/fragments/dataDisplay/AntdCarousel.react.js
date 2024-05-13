// react核心
import React from 'react';
// antd核心
import { Carousel } from 'antd';
// 辅助库
import { isString } from 'lodash';
import { pickBy } from 'ramda';
// 自定义hooks
import useCss from '../../hooks/useCss';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataDisplay/AntdCarousel.react';

/**
 * 走马灯组件AntdCarousel
 */
const AntdCarousel = (props) => {
    let {
        id,
        children,
        className,
        style,
        key,
        arrows,
        autoplay,
        dotPosition,
        easing,
        effect,
        autoplaySpeed,
        speed,
        pauseOnHover,
        infinite,
        lazyLoad,
        loading_state,
        setProps
    } = props;

    return (
        <Carousel
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
            arrows={arrows}
            autoplay={autoplay}
            dotPosition={dotPosition}
            easing={easing}
            effect={effect}
            autoplaySpeed={autoplaySpeed}
            speed={speed}
            pauseOnHover={pauseOnHover}
            infinite={infinite}
            lazyLoad={lazyLoad}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >{children}</Carousel>
    );
}

export default AntdCarousel;

AntdCarousel.defaultProps = defaultProps;
AntdCarousel.propTypes = propTypes;