# Decode and Encode WebSphere XOR Password
# Base code from: https://gist.github.com/metall0id/bb3e9bab2b7caee90cb7

try:
    import base64
    import argparse
    import sys
except:
    print "Require following Python packages:\n base64, argparse, sys\n"
    print "How to install:\npip install <package_name>\neasy_install <package_name>\n"
    sys.exit(0)

parser = argparse.ArgumentParser(description="WebSpere XOR Password Decoder/Encoder")
parser.add_argument('-e', '--encode', help='Encode password', action='store_true')
parser.add_argument('-d', '--decode', help='Decode password', action='store_true')
parser.add_argument('password', help='Password to decode/encode')
args = parser.parse_args()

return_data = ""

if args.password:
    print ""
    if args.encode:
        try:
            for character in args.password:
                return_data += chr(ord(character) ^ ord('_'))
            return_data = base64.b64encode(return_data)
            print "Decoded Password: " + args.password
            print "Encoded Password: {xor}" + return_data
        except Exception as e:
            print "Exception: " + str(e)
    elif args.decode:
        try:
            if args.password.startswith('{xor}'):
                args.password = args.password.replace('{xor}', '')
            for character in base64.b64decode(args.password):
                return_data += chr(ord(character) ^ ord('_'))
            print "Encoded Password: {xor}" + args.password
            print "Decoded Password: " + return_data
        except Exception as e:
            print "Exception: " + str(e)
    else:
        parse.print_help()
else:
    parser.print_help()