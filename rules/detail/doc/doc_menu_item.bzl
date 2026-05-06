load("//rules/detail/doc:_doc_providers.bzl", "DocMenuItem")

def _doc_menu_item_impl(ctx):
    return [
        DocMenuItem(
            name = ctx.attr.name,
            url = ctx.attr.url,
            weight = ctx.attr.weight,
            data = ctx.attr.data,
        )
    ]

doc_menu_item = rule(
    implementation = _doc_menu_item_impl,
    attrs = {
        "url": attr.string(mandatory = True),
        "weight": attr.int(default = 0),
        "data": attr.label_list(
            allow_files = True,
            default = [],
        ),
    },
)
