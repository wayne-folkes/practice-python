# Evan coding challenge

# ok i just made up a coding challenge for you
# lol
# we've got 2 dictionaries
#
# chats = {'turds odouls':set(['duncan','evan','scott']),'baseball':set(['scott','danjw','duncan']),'realnflfans':set(['scott','evan'])}
# chatnicks = {('duncan','baseball'):'yankeeboy',('duncan','turds odouls'):'poop butt',('evan','realnflfans'):'gopackgo'}
#
# chats gives a chat name and the set of members
# chatnicks gives a member,chat tuple a nickname
#
# the challenge! find everyone in chats that doesn't have a nickname. the output should be a dictionary of name to a list of channels that you don't have a nickname in
# so evan:['turds odouls'], scott:['turds odouls','baseball','realnflfans'] ...
# (a set would also make sense instead of a list)

from collections import defaultdict
import json

chats = {
    'turds odouls': set(['duncan', 'evan', 'scott']),
    'baseball': set(['scott', 'danjw', 'duncan']),
    'realnflfans': set(['scott', 'evan'])
}
chatnicks = {
    ('duncan', 'baseball'): 'yankeeboy',
    ('duncan', 'turds odouls'): 'poop butt',
    ('evan', 'realnflfans'): 'gopackgo'
}


def get_chatters():
    chatter_dict = defaultdict(list)
    for chatroom, chatters in chats.items():
        for chatter in chatters:
            chatter_dict[chatter].append(chatroom)
    return chatter_dict


if __name__ == '__main__':
    chatter_dict = get_chatters()
    for chatnick_set, chatnick in chatnicks.items():
        chatter, chatroom = chatnick_set
        chatter_dict[chatter].remove(chatroom)
    print(json.dumps(chatter_dict, sort_keys=True, indent='\t'))
