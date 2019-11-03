from bs4 import BeautifulSoup as bs
from get_soup import make_soup_from_band_name, make_soup_from_album_url
from time import sleep

#band = input("Type a band name: ")
soup = make_soup_from_band_name("cannibal corpse")

def get_albums(soup):

	"""Gets album's urls."""

	album_links = []
	albums_divs = soup.find_all("div", "album")

	for tag in albums_divs:
		a = tag.a
		album_links.append(a['href'][2:]) # every href starts with "..", so we cut it out.

	return album_links

def parse_albums(albums_list):

	"""Gets lyrics as a concatenated string of every song on album. 
	   Returns n strings, where n is a number of band's albums."""

	lyrics = []

	for album_url in albums_list:

		album_soup = make_soup_from_album_url(album_url)

		lyrics_ = album_soup.find_all("div", "lyrics")
		for lyr in lyrics_:
			to_remove = lyr.find_all(["h3", "br", "div", "a", "i"])
			for element in to_remove:
				element.decompose()

			lyrics.append(str(lyr))

	return lyrics

def return_word_count(album_urls, album_lyrics):
	ignore_list = ["the", "my", "to", "from", "this", "i", "you", "and", "for", "with", "your", "a", "an", "or", \
	"out", "in", "as", "of", "on", "will", "into", "onto", "them", "off", "are", "is", "it", "every", "have", "no", "yes", "by", "it's", \
	"their", "me", "now", "you'll", "i'll", "will", "but", "can", "we", "us", "our", "not", "could", "would", "am", "don't", "be", "has",\
	"never", "ever", "sometimes", "like", "i'm", "-", "at", "own"]

	occurences_dict = dict()

	for lyric in album_lyrics:
		words = lyric.split()

		for word in words:
			if word.lower() not in ignore_list:
				if word.lower() in occurences_dict:
					occurences_dict[word.lower()] += 1
				else:
					occurences_dict[word.lower()] = 1

	sorted_list = sorted(occurences_dict.items(), key=lambda k: k[1])
	return sorted_list

album_urls = get_albums(soup)
album_lyrics = parse_albums(album_urls)

words = return_word_count(album_urls, album_lyrics)
print(words)

