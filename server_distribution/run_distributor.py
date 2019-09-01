distributables = [
    {
        'src': 'event_listener.lua',
        'dest': '../../data/lib/core'
    },
    {
        'code': 'dofile("data/lib/core/event_listener.lua")',
        'dest': '../../data/lib/core/core.lua'
    },
    {
        'src': 'bot_onDeath.lua',
        'dest': '../../data/scripts'
    }
]

for dist in distributables:
    if dist.get('src'):
        with open(dist['dest'] + '/' + dist['src'], 'w+') as dest_file:
            with open(dist['src']) as src_file:
                dest_file.write(src_file.read())
                print(
                    'Distributable "{}" installed to "{}"'.format(
                        dist['src'],
                        dist['dest']))
    elif dist.get('code'):
        with open(dist['dest'], 'a+') as dest_file:
            dest_file.seek(0)
            if dest_file.read().find(dist['code']) != -1:
                continue
            dest_file.write('\n' + dist['code'])
            print(
                'Distributable code [{} ...] installed to {}'.format(
                    dist['code'][:15],
                    dist['dest']))

input('Press any key to exit...')
