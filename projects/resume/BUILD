load("@bazel_latex//:latex.bzl", "latex_document")

filegroup(
    name = "template",
    srcs = [
        "twentysecondcv.cls",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__fontspec",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__clearsans",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__clearsans",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__fonts__opentype__public__clear-sans",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__xkeyval",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__xkeyval",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__pstricks",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__pstricks",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__fontawesome",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__fontawesome",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__tikz",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__tikz",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__xcolor",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__textpos",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__ragged2e",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__etoolbox",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__ifmtarg",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__ifthen",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__pgffor",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__pgf",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__generic__pgf",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__marvosym",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__parskip",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__enumitem",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__hyperref",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__letltxmacro",
        # "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__xetex",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__geometry",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__smartdiagram",
    ],
    visibility = ["//visibility:public"],
)

latex_document(
    name = "resume",
    srcs = [
        "resume.tex",
        ":template",
    ],
    bib_tool = "biber",  # Is the default
    format = "pdf",  # Is the default
    main = "resume.tex",
)
