import os, sys

def main(srcfile, desfile):
    with open(srcfile) as readfh:
        with open(desfile, 'w') as writefh:
            content = readfh.readlines()

            for x in content:
                line = x[5:]
                writefh.write(line)
                



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: %s srctxt despy' % sys.argv[0]
    else:
        main(sys.argv[1], sys.argv[2])