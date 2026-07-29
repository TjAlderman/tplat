load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:packaging.bzl", "py_wheel")

py_library(
    name = "stress_tester",
    srcs = glob(["stress_tester/**/*.py"]),
    imports = ["."],
    visibility = ["//visibility:public"],
    deps = [
        requirement("pyqt5"),
        requirement("numpy"),
        requirement("paho-mqtt"),
        requirement("pandas"),
        requirement("openpyxl"),
        requirement("psutil"),
    ],
)

py_wheel(
    name = "stress_tester_whl",
    distribution = "mqtt_stress_tester",
    python_tag = "py3",
    version = "1.0.0",
    deps = [
        ":stress_tester",
    ],
    strip_path_prefixes = ["projects/mqtt/stress_tester",],
)
