load("@bazel_latex//:latex.bzl", "latex_document")

filegroup(
    name = "template",
    srcs = [
        "twentysecondcv.cls",
        "@bazel_latex_texlive//:texlive_texmf__texmf-dist__tex__latex__xcolor",
        "@bazel_latex//packages:pstricks",
        "@bazel_latex//packages:fontawesome",
        "@bazel_latex//packages:enumitem",
        "@bazel_latex//packages:letltxmacro",
        "@bazel_latex//packages:smartdiagram",
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
