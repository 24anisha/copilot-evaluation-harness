export function lookupOption(vdom, values) {
   vdom.children && vdom.children.forEach(function (el) {
        if (el.nodeName === 'option') {
            setOption(el, values)
        } else {
            lookupOption(el, values)
        } 
    })
}

function setOption(vdom, values) {
    var props = vdom.props
    if (!('disabled' in props)) {
        var value = getOptionValue(vdom, props)
            value = String(value || '').trim()
       if(typeof values === 'string'){
            props.selected = value === values
        }else{
            props.selected = values.indexOf(value) !== -1;
        }
       
        if (vdom.dom) {
            vdom.dom.selected = props.selected
            var v = vdom.dom.selected //必须加上这个,防止移出节点selected失效
        }
        
    }
}

function getOptionValue(vdom, props) {
    if (props && 'value' in props) {
        return props.value+ ''
    }
    var arr = []
    vdom.children.forEach(function (el) {
        if (el.nodeName === '#text') {
            arr.push(el.nodeValue)
        } else if (el.nodeName === '#document-fragment') {
            arr.push(getOptionValue(el))
        }
    })
    return arr.join('')
}

export function getSelectedValue(vdom, arr) {
    vdom.children.forEach(function (el) {
        if (el.nodeName === 'option') {
            if(el.props.selected === true)
               arr.push(getOptionValue(el, el.props))
        } else if (el.children) {
            getSelectedValue(el,arr)
        }
    })
    return arr
}