from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://bt-podcast.s3.amazonaws.com/itunes.xml" #VIDEO
url2 = "https://feeds.megaphone.fm/PP6777513342" #PODCAST
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://bt-podcast.s3.amazonaws.com/BigThink_logo_itunes_1400_square.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://bt-podcast.s3.amazonaws.com/BigThink_logo_itunes_1400_square.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/fe024f40-bedd-11e5-9f03-1b69bc6dac84/image/uploads_2F1561135077825-6tj4nprldn5-14731a879a248fc22016f5643ec435b0_2FThinkAgainLogoFinal3000x3000-2019.jpg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/fe024f40-bedd-11e5-9f03-1b69bc6dac84/image/uploads_2F1561135077825-6tj4nprldn5-14731a879a248fc22016f5643ec435b0_2FThinkAgainLogoFinal3000x3000-2019.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup2)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
