# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725638810.1007895
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n</style>\n')
        if len(translations) > 1:
            pass
            for langname in translations.keys():
                pass
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\n\nfunction renderGallery() {\n    var container = document.getElementById("gallery_container");\n    container.innerHTML = \'\';\n    var layoutGeometry = require(\'justified-layout\')(jsonContent, {\n    "containerWidth": container.offsetWidth,\n    "targetRowHeight": ')
        __M_writer(str(thumbnail_size))
        __M_writer('*.6,\n    "boxSpacing": 5});\n    container.style.height = layoutGeometry.containerHeight + \'px\';\n    var boxes = layoutGeometry.boxes;\n    for (var i = 0; i < boxes.length; i++) {\n        var img = document.createElement("img");\n        img.setAttribute(\'src\', jsonContent[i].url_thumb);\n        img.setAttribute(\'alt\', jsonContent[i].title);\n        img.style.width = boxes[i].width + \'px\';\n        img.style.height = boxes[i].height + \'px\';\n        link = document.createElement("a");\n        link.setAttribute(\'href\', jsonContent[i].url);\n        link.setAttribute(\'class\', \'image-reference\');\n        div = document.createElement("div");\n        div.setAttribute(\'class\', \'image-block\');\n        div.setAttribute(\'title\', jsonContent[i].title);\n        div.setAttribute(\'data-toggle\', "tooltip")\n        div.style.width = boxes[i].width + \'px\';\n        div.style.height = boxes[i].height + \'px\';\n        div.style.top = boxes[i].top + \'px\';\n        div.style.left = boxes[i].left + \'px\';\n        link.append(img);\n        div.append(link);\n        container.append(div);\n    }\n    baguetteBox.run(\'#gallery_container\', {\n        captions: function(element) {\n            return element.getElementsByTagName(\'img\')[0].alt;\n    }});\n}\nrenderGallery();\nwindow.addEventListener(\'resize\', renderGallery);\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "32": 0, "65": 2, "66": 3, "67": 4, "72": 5, "77": 39, "82": 59, "87": 104, "93": 5, "106": 7, "124": 7, "125": 8, "126": 8, "127": 9, "128": 10, "129": 10, "130": 10, "131": 12, "132": 13, "133": 14, "134": 14, "135": 17, "136": 18, "137": 19, "138": 20, "139": 20, "140": 20, "141": 20, "142": 20, "143": 22, "144": 24, "145": 26, "146": 27, "147": 29, "148": 30, "149": 30, "150": 30, "151": 30, "152": 30, "153": 31, "154": 31, "155": 31, "156": 31, "157": 33, "158": 36, "159": 37, "160": 37, "166": 41, "180": 41, "181": 42, "182": 42, "183": 52, "185": 53, "187": 54, "188": 55, "189": 55, "190": 55, "191": 55, "192": 55, "198": 61, "208": 61, "209": 64, "210": 64, "211": 71, "212": 71, "218": 212}}
__M_END_METADATA
"""