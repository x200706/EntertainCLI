import argparse
from cmd.test import test


def main():
  parser = argparse.ArgumentParser()
  subcmd = parser.add_subparsers(dest='subcmd', help='說明', metavar='指令')

  #---在這裡添加parser---#
  test_parser = subcmd.add_parser('test', help='測試用指令，可選-t引數')
  test_parser.set_defaults(func=test)

  args, remaining_args = parser.parse_known_args()

  if hasattr(args, 'func'):
    args.func(remaining_args)
  else:
    parser.print_help()

if __name__ == "__main__":
  main()
