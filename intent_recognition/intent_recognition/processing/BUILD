licenses(["notice"])

package(default_visibility = ["//visibility:public"])

mediapipe_proto_library(
    name = "filter_annotated_recording_collection_calculator_proto",
    srcs = ["filter_annotated_recording_collection_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = ["@mediapipe//mediapipe/framework:calculator_proto"],
)

mediapipe_proto_library(
    name = "extract_sensor_data_from_annotated_recording_collection_calculator_proto",
    srcs = ["extract_sensor_data_from_annotated_recording_collection_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = [
        "//intent_recognition:annotated_recording_collection_sensor_options_proto",
        "@mediapipe//mediapipe/framework:calculator_proto",
    ],
)

mediapipe_proto_library(
    name = "merge_sensor_data_into_annotated_recording_collection_calculator_proto",
    srcs = ["merge_sensor_data_into_annotated_recording_collection_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = [
        "//intent_recognition:annotated_recording_collection_sensor_options_proto",
        "@mediapipe//mediapipe/framework:calculator_proto",
    ],
)

mediapipe_proto_library(
    name = "window_calculator_proto",
    srcs = ["window_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = [
        "@mediapipe//mediapipe/framework:calculator_proto",
    ],
)

mediapipe_proto_library(
    name = "set_annotated_recording_collection_metadata_calculator_proto",
    srcs = ["set_annotated_recording_collection_metadata_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = [
        "//intent_recognition:annotated_recording_collection_sensor_options_proto",
        "@mediapipe//mediapipe/framework:calculator_proto",
    ],
)

mediapipe_proto_library(
    name = "compute_sample_magnitude_variance_calculator_proto",
    srcs = ["compute_sample_magnitude_variance_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = ["@mediapipe//mediapipe/framework:calculator_proto"],
)

cc_library(
    name = "compute_sample_magnitude_variance_calculator",
    srcs = ["compute_sample_magnitude_variance_calculator.cc"],
    deps = [
        ":compute_sample_magnitude_variance_calculator_cc_proto",
        "@com_github_glog_glog//:glog",
        "@com_google_absl//absl/status",
        "@mediapipe//mediapipe/framework:calculator_framework",
    ],
    alwayslink = 1,
)

mediapipe_proto_library(
    name = "drop_on_threshold_value_calculator_proto",
    srcs = ["drop_on_threshold_value_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = ["@mediapipe//mediapipe/framework:calculator_proto"],
)

cc_library(
    name = "drop_on_threshold_value_calculator",
    srcs = ["drop_on_threshold_value_calculator.cc"],
    deps = [
        ":drop_on_threshold_value_calculator_cc_proto",
        "@com_github_glog_glog//:glog",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/strings",
        "@mediapipe//mediapipe/framework:calculator_cc_proto",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:calculator_options_cc_proto",
    ],
    alwayslink = 1,
)

mediapipe_proto_library(
    name = "processing_options_proto",
    srcs = ["processing_options.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = [
        ":drop_on_threshold_value_calculator_proto",
        ":window_calculator_proto",
    ],
)

proto_library(
    name = "string_label_class_map",
    srcs = ["string_label_class_map.proto"],
)

cc_proto_library(
    name = "string_label_class_map_cc_proto",
    deps = [":string_label_class_map"],
)

mediapipe_proto_library(
    name = "class_mappings_side_packet_calculator_proto",
    srcs = ["class_mappings_side_packet_calculator.proto"],
    def_java_lite_proto = False,
    def_options_lib = False,
    def_portable_proto = False,
    deps = ["@mediapipe//mediapipe/framework:calculator_proto"],
)

cc_library(
    name = "filter_annotated_recording_collection_calculator",
    srcs = ["filter_annotated_recording_collection_calculator.cc"],
    deps = [
        ":filter_annotated_recording_collection_calculator_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_utils",
        "@com_github_glog_glog//:glog",
        "@com_google_absl//absl/algorithm:container",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/container:flat_hash_set",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/strings",
        "@com_google_absl//absl/time",
        "@com_google_protobuf//:protobuf",
        "@mediapipe//mediapipe/framework:calculator_framework",
    ],
    alwayslink = 1,
)

cc_library(
    name = "extract_sensor_data_from_annotated_recording_collection_calculator",
    srcs = ["extract_sensor_data_from_annotated_recording_collection_calculator.cc"],
    deps = [
        ":extract_sensor_data_from_annotated_recording_collection_calculator_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_sensor_options_cc_proto",
        "//intent_recognition:annotated_recording_collection_utils",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/time",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:calculator_options_cc_proto",
    ],
    alwayslink = 1,
)

cc_library(
    name = "merge_sensor_data_into_annotated_recording_collection_calculator",
    srcs = ["merge_sensor_data_into_annotated_recording_collection_calculator.cc"],
    deps = [
        ":merge_sensor_data_into_annotated_recording_collection_calculator_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_sensor_options_cc_proto",
        "//intent_recognition:annotated_recording_collection_utils",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/strings:str_format",
        "@com_google_absl//absl/time",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:calculator_options_cc_proto",
    ],
    alwayslink = 1,
)

cc_library(
    name = "window_calculator",
    srcs = ["window_calculator.cc"],
    deps = [
        ":window_calculator_cc_proto",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/status:statusor",
        "@com_google_absl//absl/strings:str_format",
        "@com_google_absl//absl/types:optional",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:calculator_options_cc_proto",
    ],
    alwayslink = 1,
)

cc_library(
    name = "class_mappings_side_packet_calculator",
    srcs = ["class_mappings_side_packet_calculator.cc"],
    deps = [
        ":class_mappings_provider_hdr",
        ":class_mappings_side_packet_calculator_cc_proto",
        ":string_label_class_mappings_provider",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/status",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:packet",
    ],
    alwayslink = 1,
)

cc_library(
    name = "add_class_mappings_calculator",
    srcs = ["add_class_mappings_calculator.cc"],
    deps = [
        ":class_mappings_provider_hdr",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/strings",
        "@mediapipe//mediapipe/framework:calculator_framework",
    ],
    alwayslink = 1,
)

cc_library(
    name = "set_annotated_recording_collection_metadata_calculator",
    srcs = ["set_annotated_recording_collection_metadata_calculator.cc"],
    deps = [
        ":set_annotated_recording_collection_metadata_calculator_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_sensor_options_cc_proto",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/container:flat_hash_set",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/strings",
        "@com_google_absl//absl/strings:str_format",
        "@com_google_protobuf//:protobuf",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:calculator_options_cc_proto",
    ],
    alwayslink = 1,
)

cc_library(
    name = "class_mappings_provider_hdr",
    hdrs = ["class_mappings_provider.h"],
    deps = [
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/status:statusor",
    ],
)

cc_library(
    name = "class_mappings_provider_helpers",
    hdrs = ["class_mappings_provider_helpers.h"],
    deps = [
        "@com_github_glog_glog//:glog",
        "@com_google_absl//absl/container:flat_hash_map",
    ],
)

cc_library(
    name = "string_label_class_mappings_provider_helpers",
    hdrs = ["string_label_class_mappings_provider_helpers.h"],
    deps = [
        ":string_label_class_map_cc_proto",
        ":string_label_class_mappings_provider",
        "@com_google_absl//absl/status:statusor",
    ],
)

cc_library(
    name = "string_label_class_mappings_provider",
    srcs = ["string_label_class_mappings_provider.cc"],
    hdrs = [
        "string_label_class_mappings_provider_helpers.h",
    ],
    deps = [
        ":class_mappings_provider_hdr",
        ":class_mappings_provider_helpers",
        ":string_label_class_map_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_utils",
        "@com_google_absl//absl/container:flat_hash_map",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/status:statusor",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
    ],
    alwayslink = 1,
)

cc_binary(
    name = "process_annotated_recording_collection_main",
    srcs = ["process_annotated_recording_collection_main.cc"],
    deps = [
        ":add_class_mappings_calculator",
        ":class_mappings_side_packet_calculator",
        ":class_mappings_side_packet_calculator_cc_proto",
        ":compute_sample_magnitude_variance_calculator",
        ":drop_on_threshold_value_calculator",
        ":extract_sensor_data_from_annotated_recording_collection_calculator",
        ":filter_annotated_recording_collection_calculator",
        ":filter_annotated_recording_collection_calculator_cc_proto",
        ":merge_sensor_data_into_annotated_recording_collection_calculator",
        ":merge_sensor_data_into_annotated_recording_collection_calculator_cc_proto",
        ":processing_options_cc_proto",
        ":set_annotated_recording_collection_metadata_calculator",
        ":window_calculator",
        ":window_calculator_cc_proto",
        "//intent_recognition:annotated_recording_collection_cc_proto",
        "//intent_recognition:annotated_recording_collection_sensor_options_cc_proto",
        "//intent_recognition:annotated_recording_collection_utils",
        "@com_github_glog_glog//:glog",
        "@com_google_absl//absl/flags:flag",
        "@com_google_absl//absl/flags:parse",
        "@com_google_absl//absl/status",
        "@com_google_absl//absl/status:statusor",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@mediapipe//mediapipe/calculators/core:packet_resampler_calculator",
        "@mediapipe//mediapipe/framework:calculator_cc_proto",
        "@mediapipe//mediapipe/framework:calculator_framework",
        "@mediapipe//mediapipe/framework:packet",
        "@riegeli//riegeli/bytes:fd_reader",
        "@riegeli//riegeli/bytes:fd_writer",
        "@riegeli//riegeli/bytes:read_all",
        "@riegeli//riegeli/messages:text_parse_message",
        "@riegeli//riegeli/records:record_reader",
        "@riegeli//riegeli/records:record_writer",
    ],
)
