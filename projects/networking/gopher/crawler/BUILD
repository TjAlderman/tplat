load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:packaging.bzl", "py_wheel")

py_library(
    name = "crawler",
    srcs = glob(["crawler/**/*.py"]),
    imports = ["."],
    visibility = ["//visibility:public"],
)

py_wheel(
    name = "crawler_whl",
    distribution = "gopher_crawler",
    python_tag = "py3",
    version = "1.0.0",
    deps = [
        ":crawler",
    ],
    strip_path_prefixes = ["projects/gopher/crawler",],
)
