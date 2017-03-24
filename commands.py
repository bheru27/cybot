# -*- coding: utf-8 -*-
import os
import fourchan_json
import fourchan_pic
import random
import string
import re
import reddit
from nltk.tag import pos_tag
import time
import requests
from bs4 import BeautifulSoup

class tcol:
        NORMAL = "\u000f"
        BOLD = "\u0002"
        UNDERLINE = "\u001f"
        REVERSE = "\u0016"
        WHITE = "\u00030"
        BLACK = "\u00031"
        DARK_BLUE = "\u00032"
        DARK_GREEN = "\u00033"
        RED = "\u00034"
        BROWN = "\u00035"
        GREEN = "\u00039"


def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size
    random_point = random.randint(0, total_bytes)
    xfile = open(file_name)
    xfile.seek(random_point)
    c = xfile.read(1)
    s = ""
    while c != ".":
        c = xfile.read(1)

    xfile.read(1)
    c = xfile.read(1)
    while c == ".":
        xfile.read(1)
    while c != ".":
        if c != "\n":
            if c != "\r":
                s += c
            else:
                s += " "
        else:
            s += " "
        c = xfile.read(1)
    s += c
    c = xfile.read(1)
    s += c
    while c == ".":
        s += c
        c = xfile.read(1)
    s.replace("- ", " ")
    s = re.sub('\s+', ' ', s)
    return s


def getuser(ircmsg):
    return ircmsg.split(":")[1].split('!')[0]


_command_dict = {}


def command(name):
    # The decorator appending all fn's to a dict
    def _(fn):
        # Decorators return an inner function whom we
        # pass the function.
        _command_dict[name] = fn
    return _


def nothing(args):
    return ""


def get_command(name):
    # Explicity over implicity?
    # Fuck that

    # We just lower the string.
    # and check later its upper cased
    if name.lower() in _command_dict:
        return _command_dict[name.lower()]
    else:
        return nothing


def twitter(args):
    print(args["args"], type(args["args"]))
    if type(args["args"]) is not str:
        tweet = " ".join(args["args"])
        sendmsg = args["sendmsg"]
        channel = args["channel"]
    else:
        tweet = args
    r = requests.post("http://carta.im/tweetproxy/", data={'tweet': tweet[:139]})
    if "200" in r.text:
        return tweet[:139] + " @proxytwt"
    else:
        return ":( pls fix me ;-;"

def random_image(image_link):
    """
    Opens a directory with images using bs4.
    Then picks one value from list of images.
    """
    img_list = []
    soup = BeautifulSoup(requests.get(image_link).text, "html.parser")
    for i in soup.findAll("a"):
        parsed = image_link+i['href']
        img_list.append(parsed)
    img_link = random.choice(img_list)
    return img_link

def imgur_pic(subreddit):
    html = BeautifulSoup(requests.get("http://imgur.com/r/{}/".format(subreddit)).text, "html.parser")
    length = len(html.findAll("a", {"class": "image-list-link"}))
    retval = ""
    try:
        retval = "https://imgur.com{}".format(html.findAll("a", {"class": "image-list-link"})[random.randint(0, length)]['href'])
    except IndexError:
        pass
    return retval

@command("ayylmao")
def ayylmao(args):
    sendmsg = args["sendmsg"]
    line = ('ABDUCTION: INCOMING')

    ayylien = ["       .-""""-.        .-""""-.    ",
               "      /        \      /        \   ",
               "     /_        _\    /_        _\  ",
               "    // \      / \\  // \      / \\ ",
               "    |\__\    /__/|  |\__\    /__/| ",
               "     \    ||    /    \    ||    /  ",
               "      \        /      \        /   ",
               "       \  __  /        \  __  /    ",
               "        '.__.' ayy lmao '.__.'     "]


    ircmsg = args["raw"]
    user = ircmsg.split(":")[1].split('!')[0]
    channel = args["channel"]
    sendmsg(channel, line)
    for lines in ayylien:
        sendmsg(user, lines)
        time.sleep(1)
   # ayy lmao
   # Doing all the logic inside the function
   # Since sendmsg wont post empty strings.
    return ""

@command("feel")
def feel(args):  # >tfw
    sendmsg = args["sendmsg"]
    line = ('"tfw no gf" is an abbreviated expression for "that feeling [I get] '
              'when [I have] no girlfriend" often used in online discussions and '
              'comments.')

    feelguy  = ["░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░",
                "░░░░▄▀▀░░░░░░░░░░░░░▀▄░░░░░░░",
                "░░▄▀░░░░░░░░░░░░░░░░░░▀▄░░░░░",
                "░░█░░░░░░░░░░░░░░░░░░░░░▀▄░░░",
                "░▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌░░",
                "░█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█░░",
                "▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌░",
                "█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█░",
                "█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌",
                "▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌",
                "░█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░▀▄",
                "░▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█",
                "░░▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█",
                "░░░█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌",
                "░░░▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀░",
                "░░░▐▌░░▐▀▄░░░░░░░░░░░░░░░░█░░",
                "░░░▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█░░░",
                "░░░█░░░▀░░░░▀▄░░░░░░░░░░▄▀░░░",
                "░░▐▌░░░░░░░░░░▀▄░░░░░░▄▀░░░░░",
                "░▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀░░░░░░░",
                "▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄"]


    ircmsg = args["raw"]
    user = ircmsg.split(":")[1].split('!')[0]
    channel = args["channel"]
    sendmsg(channel, line)
    for lines in feelguy:
        sendmsg(user, lines)
        time.sleep(1)
    # Doing all the logic inside the function
    # Since sendmsg wont post empty strings.
    return ""

@command("wake")
def wake(args):
    return "(can't wake up)"


@command("guinea")
def guinea(args):
    directory = os.path.dirname(__file__)
    guinea = directory + os.path.join("/texts/other/guinea.txt")
    return random.choice(list(open(guinea)))

@command("guineas")
def guinea(args):
    return imgur_pic("guineapigs")

@command("cat")
def cat(args):
    return imgur_pic("cats")

@command("checkem")
def checkem(args):
    not_dubs = random.randint(0, 99)
    return str(not_dubs).zfill(2)

@command("eightball")
def eight(args):
    directory = os.path.dirname(__file__)
    eight = directory + os.path.join("/texts/other/eightball.txt")
    return random.choice(list(open(eight)))


@command("triforce")
def coolt(args):
    sendmsg = args["sendmsg"]
    channel = args["channel"]
    spaces1 = random.randint(1,5)
    spaces2 = random.randint(1,3)
    string1 = (" "*spaces1 + ("▲"))
    string2 = (" "*spaces2 + ("▲ ▲"))
    sendmsg(channel, string1)
    sendmsg(channel, string2)
    return ""

@command("booty")
def booty(args):
    return "( ͡° ͜ʖ ͡°)"


@command("shrug")
def shrug(args):
    return "¯\_(ツ)_/¯"

@command("denko")
def denko(args):
    return "(´･ω･`)"


@command("cute")
def cute(args):
    user = getuser(args["raw"])
    args = args["args"]
    if len(args) < 1:
        cutelist = ["✿◕ ‿ ◕✿", "❀◕ ‿ ◕❀", "(✿◠‿◠)",
                    "(◕‿◕✿) ", "( ｡◕‿◕｡)", "(◡‿◡✿)",
                    "⊂◉‿◉つ ❤", "{ ◕ ◡ ◕}", "( ´・‿-) ~ ♥",
                    "(っ⌒‿⌒)っ~ ♥", "ʕ´•ᴥ•`ʔσ”", "(･Θ･) caw",
                    "(=^･ω･^)y＝", "ヽ(=^･ω･^=)丿", "~(=^･ω･^)ヾ(^^ )",
                    "| (•□•) | (❍ᴥ❍ʋ)", "ϞϞ(๑⚈ ․̫ ⚈๑)∩", "ヾ(･ω･*)ﾉ",
                    "▽・ω・▽ woof~", "(◎｀・ω・´)人(´・ω・｀*)", "(*´・ω・)ノ(-ω-｀*)",
                    "(❁´ω`❁)", "(＊◕ᴗ◕＊)", "{´◕ ◡ ◕｀}", "₍•͈ᴗ•͈₎",
                    "(˘･ᴗ･˘)", "(ɔ ˘⌣˘)˘⌣˘ c)", "(⊃｡•́‿•̀｡)⊃", "(´ε｀ )♡",
                    "(◦˘ З(◦’ںˉ◦)♡", "( ＾◡＾)っ~ ❤ Leper",
                    "╰(　´◔　ω　◔ `)╯", "(*･ω･)", "(∗•ω•∗)", "( ◐ω◐ )"]
    else:
        args = " ".join(args)
        cutelist = ["(✿◠‿◠)っ~ ♥ " + args, "⊂◉‿◉つ ❤ " + args, "( ´・‿-) ~ ♥ " + args,
                    "(っ⌒‿⌒)っ~ ♥ " + args, "ʕ´•ᴥ•`ʔσ” BEARHUG " + args,
                    user + " ~(=^･ω･^)ヾ(^^ ) " + args, user + " (◎｀・ω・´)人(´・ω・｀*) " + args,
                    user + " (*´・ω・)ノ(-ω-｀*) " + args,
                    user + " (ɔ ˘⌣˘)˘⌣˘ c) " + args,
                    "(⊃｡•́‿•̀｡)⊃ U GONNA GET HUGGED " + args, args + " (´ε｀ )♡",
                    user + " (◦˘ З(◦’ںˉ◦)♡ " + args, "( ＾◡＾)っ~ ❤ " + args]
    return random.choice(cutelist)

@command("bots")
def bots(args):
    return "Reporting in! [Python] Try .cybhelp for commands."

@command("spikepig")
def spikepig(args):
    return imgur_pic("hedgehog")

@command("r8")
def random_rate(args):
    message = args["args"]
    give_rating = random.randint(0, 1)
    message = pos_tag(message)
    print(message)
    nounlist = []
    for word, tag in message:
        if tag == "NNP" or tag == "NN":
            nounlist.append(word)
    if not nounlist:
        nounlist.append("nothings")
    word = nounlist[random.randint(0, len(nounlist)-1)]
    rating = random.randint(0, 10)
    if give_rating or nounlist[0] == "nothings":
        return str(rating) + "/10"
    else:
        return word + "/10"

@command("just")
def just(args):
	return "...type it yourself..."

@command("spooky")
def spooky(args):
    directory = os.path.dirname(__file__)
    spook = directory + os.path.join("/texts/other/spooks.txt")
    return random.choice(list(open(spook)))

def breaklines(str):  # This function breaks lines at \n and sends the split lines to where they need to go
    strarray = string.split(str, "\n")
    return strarray

# in place case-preserving function
def replacement_func(match, repl_pattern):
    match_str = match.group(0)
    repl = ''.join([r_char if m_char.islower() else r_char.upper()
                   for r_char, m_char in zip(repl_pattern, match_str)])
    repl += repl_pattern[len(match_str):]
    return repl

bicd ={"epic":"ebin",
        "penis":"benis",
        "wh":"w",
        "th":"d",
        "af":"ab",
        "ap":"ab",
        "ca":"ga",
        "ck":"gg",
        "co":"go",
        "ev":"eb",
        "ex":"egz",
        "et":"ed",
        "iv":"ib",
        "it":"id",
        "ke":"ge",
        "nt":"nd",
        "op":"ob",
        "ot":"od",
        "po":"bo",
        "pe":"be",
        "pi":"bi",
        "up":"ub",
        "va":"ba",
        "cr":"gr",
        "kn":"gn",
        "lt":"ld",
        "mm":"m",
        "nt":"dn",
        "pr":"br",
        "ts":"dz",
        "tr":"dr",
        "bs":"bz",
        "ds":"dz",
        "fs":"fz",
        "gs":"gz",
        "is":"iz",
        "ls":"lz",
        "ms":"mz",
        "ns":"nz",
        "rs":"rz",
        "ss":"sz",
        "ts":"tz",
        "us":"uz",
        "ws":"wz",
        "ys":"yz",
        "alk":"olk",
        "ing":"ign",
        "ic":"ig",
        "ng":"nk",
        "kek":"geg",
        "some":"sum",
        "meme":"maymay"
}
ebinFaces = [ ':D', ':DD', ':DDD', ':-D', 'XD', 'XXD', 'XDD', 'XXDD' ];
@command("spurd")
def spurd(args):
	new_args = " ".join(args["args"])
	for k, v in bicd.items():
		new_args = re.sub(k, lambda k: replacement_func(k,v), new_args, flags=re.I)
	return new_args+" "+ random.choice(ebinFaces)

@command("1337")
def leetspeak(args):
    input = " ".join(args["args"])

    if input.strip() == "":
        input = random.choice(["elite", "leet", "hacks", "hax", "cyb as fuck"])

    # adapted from
    # https://scripts.irssi.org/scripts/dau.pl
    # line 2943
    output = re.sub(r'fucker', 'f@#$er', input, flags=re.I|re.U)
    output = re.sub(r'hacker', 'h4x0r', output, flags=re.I|re.U)
    output = re.sub(r'sucker', 'sux0r', output, flags=re.I|re.U)
    output = re.sub(r'fear', 'ph34r', output, flags=re.I|re.U)

    output = re.sub(r'\b(?P<q>\w+)ude\b', r'\g<q>00d', output, flags=re.I|re.U)
    output = re.sub(r'\b(?P<q>\w+)um\b', r'\g<q>00m', output, flags=re.I|re.U)
    output = re.sub(r'\b(?P<q>\w{3,})er\b', r'\g<q>0r', output, flags=re.I|re.U)
    output = re.sub(r'\bdo\b', r'd00', output, flags=re.I|re.U)
    output = re.sub(r'\bthe\b', r'teh', output, flags=re.I|re.U)
    output = re.sub(r'\byou\b', r'j00', output, flags=re.I|re.U)

    output = output.translate(str.maketrans("lLzZeEaAsSgGtTbBqQoOiIcC", "11223344556677889900||(("))
    if random.randrange(0,2) == 1:
        output = output.lower()
    else:
        output = output.upper()
    return output
