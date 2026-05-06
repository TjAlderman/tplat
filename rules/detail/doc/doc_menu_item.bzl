load("//rules/detail/doc:_doc_providers.bzl", "DocMenuItem")

def _doc_menu_item_impl(ctx):
    url = ctx.attr.url
    page_ref = ctx.attr.pageRef

    if not url and not page_ref:
        fail("Either 'url' or 'pageRef' must be specified.")

    return [
        DocMenuItem(
            name = ctx.attr.name,
            url = url,
            pageRef = page_ref,
            weight = ctx.attr.weight,
            data = ctx.attr.data,
        )
    ]

doc_menu_item = rule(
    implementation = _doc_menu_item_impl,
    attrs = {
        "url": attr.string(),
        "pageRef": attr.string(),
        "weight": attr.int(default = 0),
        "data": attr.label_list(
            allow_files = True,
            default = [],
        ),
    },
)
