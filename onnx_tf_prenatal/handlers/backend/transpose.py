import tensorflow as tf

from onnx_tf_prenatal.handlers.backend_handler import BackendHandler
from onnx_tf_prenatal.handlers.handler import onnx_op
from onnx_tf_prenatal.handlers.handler import tf_func


@onnx_op("Transpose")
@tf_func(tf.transpose)
class Transpose(BackendHandler):

  @classmethod
  def version_1(cls, node, **kwargs):
    return [cls.make_tensor_from_onnx_node(node, **kwargs)]

  @classmethod
  def version_13(cls, node, **kwargs):
    return [cls.make_tensor_from_onnx_node(node, **kwargs)]
