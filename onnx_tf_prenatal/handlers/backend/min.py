import tensorflow as tf

from onnx_tf_prenatal.common import exception
from onnx_tf_prenatal.common import data_type
from onnx_tf_prenatal.common import sys_config
from onnx_tf_prenatal.handlers.backend_handler import BackendHandler
from onnx_tf_prenatal.handlers.handler import onnx_op


@onnx_op("Min")
class Min(BackendHandler):
  supported_types = [
      tf.bfloat16, tf.float16, tf.float32, tf.float64, tf.int32, tf.int64
  ]
  cast_map = {
      tf.uint8: tf.int32,
      tf.uint16: tf.int32,
      tf.uint32: tf.int64,
      tf.int8: tf.int32,
      tf.int16: tf.int32
  }

  @classmethod
  def args_check(cls, node, **kwargs):
    # update cast map based on the auto_cast config option
    cls.cast_map[tf.uint64] = tf.int64 if sys_config.auto_cast else None

    inp_dtype = kwargs["tensor_dict"][node.inputs[0]].dtype

    if inp_dtype in cls.cast_map and cls.cast_map[inp_dtype] is None:
      exception.DTYPE_NOT_CAST_EXCEPT(
          "Min input " + node.inputs[0] + " with data type '" +
          data_type.tf_to_np_str(inp_dtype) + "'",
          data_type.tf_to_np_str_list(cls.supported_types))

  @classmethod
  def _common(cls, node, **kwargs):
    values = [kwargs["tensor_dict"][inp] for inp in node.inputs]
    dtype = values[0].dtype
    if dtype in cls.cast_map:
      values = [tf.cast(v, cls.cast_map[dtype]) for v in values]
    result = values[0]
    for i in range(1, len(values)):
      result = tf.minimum(result, values[i])
    return [tf.cast(result, dtype) if dtype in cls.cast_map else result]

  @classmethod
  def version_1(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_6(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_8(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_12(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_13(cls, node, **kwargs):
    return cls._common(node, **kwargs)
