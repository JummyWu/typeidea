let widget = document.getElementsByClassName('markdownx-widget')[0];
let element = document.getElementsByClassName('markdownx');
let element_divs = element[0].getElementsByTagName('div');
let div_editor = element_divs[0];
let div_preview = element_divs[1];

let navbar_bar = document.getElementsByClassName('markdownx-toolbar')[0].getElementsByTagName('li');
let btn_preview = navbar_bar[0];
let btn_fullscreen = navbar_bar[1];

var turn_active = function(element) {
    value = element.classname;
    classval = element.getAttribute('class');
    if (value.indexOf('active') >= 0) {
        element.removeClass('active');
    }
    else {
        value += 'active'
    }
}

var refresh_pretty = function() { 
    // 每次有都需要重新渲染code
    PR.prettyPrint();
};

var enable_preview = function() {
    var class_btn_preview = btn_preview.getAttribute('class');
    var index = class_btn_preview.indexOf('active');
    if (index >= 0) {
        btn_preview.setAttribute('class', '');
        div_editor.setAttribute('class', 'col-md-12 child-left');
        div_preview.style.display = 'none';
    } 
    else {
        btn_preview.setAttribute('class', 'active');
        div_editor.setAttribute('class', 'col-md-6 child-left');
        div_preview.style.display = 'block';
    }
};

var enable_fullscreen = function() {
    var class_btn_fullscreen = btn_fullscreen.getAttribute('class');
    var index = class_btn_fullscreen.indexOf('active');
    if (index >= 0) {
        btn_fullscreen.setAttribute('class', '');
        widget.setAttribute('class', 'markup-widget');    
    }
    else{
        btn_fullscreen.setAttribute('class', 'active');
        widget.setAttribute('class', 'markup-widget fullscreen');    
    }
}

Object.keys(element).map(key =>
        element[key].addEventListener('markdownx.update', refresh_pretty)
);

btn_preview.addEventListener('click', enable_preview);
btn_fullscreen.addEventListener('click', enable_fullscreen);
