print(type(0))

print(type('0'))

protocol = input('* Enter the protocol to filter by (arp | bootp | icmp | dns | 0 - is all): ')
if (protocol.lower() == 'arp') or (protocol.lower() == 'bootp') or (protocol.lower() == 'icmp') or (protocol.lower() == 'dns'):
    print(f'\nThe program will capture only {protocol.upper()} packets.')
elif protocol == '0':
    print('\nThe program will capture all protocols.\n')
else:
    print('\nERROR: input does not match any of these (arp | bootp | icmp | dns | 0 - is all)')
    # sys.exit()
print(protocol)
print(type(protocol))
