import argparse


def test(args):
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--test', action='store_true')

  sub_args = parser.parse_args(args)

  if sub_args.test:
      print('測試用指令 有帶引數')
  else:
      print('測試用指令 沒帶引數')
  
