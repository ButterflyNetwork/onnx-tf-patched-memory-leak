import argparse
import sys

import onnx_tf_prenatal.converter


def main():
  args = sys.argv[1:]
  parser = argparse.ArgumentParser(
      description="ONNX-Tensorflow Command Line Interface")
  parser.add_argument(
      "command",
      choices=["convert"],
      help="Available commands.")

  if len(args) == 0:
    parser.parse_args(["-h"])
  cli_tool = parser.parse_args([args[0]])
  if cli_tool.command == "convert":
    return onnx_tf_prenatal.converter.main(args[1:])


if __name__ == '__main__':
  main()
