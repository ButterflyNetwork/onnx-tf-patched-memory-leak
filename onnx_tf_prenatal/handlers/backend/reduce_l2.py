import tensorflow as tf

from onnx_tf_prenatal.handlers.backend_handler import BackendHandler
from onnx_tf_prenatal.handlers.handler import onnx_op
from onnx_tf_prenatal.handlers.handler import tf_func
from .math_mixin import ReductionMixin


@onnx_op("ReduceL2")
@tf_func(tf.norm)
class ReduceL2(ReductionMixin, BackendHandler):

  @classmethod
  def get_attrs_processor_param(cls):
    return {"default": {"ord": 2}}

  @classmethod
  def version_1(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_11(cls, node, **kwargs):
    return cls._common(node, **kwargs)

  @classmethod
  def version_13(cls, node, **kwargs):
    return cls._common(node, **kwargs)
