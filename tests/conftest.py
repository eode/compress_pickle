import pytest
from fixtures import (
    random_message,
    compressions,
    wrong_compressions,
    valid_extensions,
    invalid_extensions,
    file,
    unhandled_extensions,
    set_default_extension,
    file_compressions,
    picklers_to_validate,
    file_types,
    pickler_method,
    compressions_to_validate,
    preprocess_path_on_path_types,
    preprocess_path_on_file_types,
    preprocess_path_on_file_types_and_compressions,
    dump_load,
    simple_dump_and_remove,
    hijack_lz4,
    hijack_dill,
    hijack_cloudpickle,
)
