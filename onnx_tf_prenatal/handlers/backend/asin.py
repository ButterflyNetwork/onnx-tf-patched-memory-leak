import tensorflow as tf

from onnx_tf_prenatal.handlers.backend_handler import BackendHandler
from onnx_tf_prenatal.handlers.handler import onnx_op
from onnx_tf_prenatal.handlers.handler import tf_func
from .math_mixin import BasicMathMixin


@onnx_op("Asin")
@tf_func(tf.asin)
class Asin(BasicMathMixin, BackendHandler):

  @classmethod
  def version_7(cls, node, **kwargs):
    return [cls.make_tensor_from_onnx_node(node, **kwargs)]
