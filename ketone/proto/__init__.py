# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

def _check_onnx_version():
    import pkg_resources
    min_required_version = pkg_resources.parse_version('1.0.1')
    current_version = pkg_resources.get_distribution('onnx').parsed_version
    assert current_version >= min_required_version , 'ONNXMLTools requires ONNX version 1.0.1 or a newer one'
_check_onnx_version()

# Rather than using ONNX protobuf definition throughout our codebase, we import ONNX protobuf definition here so that
# we can conduct quick fixes by overwriting ONNX functions without changing any lines elsewhere.
import onnx
from onnx import onnx_pb as onnx_proto
from onnx import helper


def get_opset_number_from_onnx():
    return onnx.defs.onnx_opset_version()
