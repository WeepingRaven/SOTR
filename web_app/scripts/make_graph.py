import matplotlib
matplotlib.use('Agg')

import os
from web_app import OUTPUT_FOLDER
# album_urls = get_albums(soup)
# album_lyrics = parse_albums(album_urls)

#counted_words = return_word_count(album_lyrics)
#counted_words = [('rising', 6), ('awake', 6), ('old', 5), ('running', 4), ('tears', 3), ('drop', 2), ('walls', 1), ('reunite,', 1), ('implode,', 1), ('explode,', 1)]

def save_graph(counted_words, band, results_num=10, ):
	from matplotlib import pyplot as plt
	names = [counted_words[x][0] for x in range(results_num)]
	values = [counted_words[x][1] for x in range(results_num)]

	plt.style.use('seaborn-dark')
	plt.figure(figsize=(9, 3))
	plt.plot(values[0])
	plt.bar(names, values)
	plt.suptitle(f"Words of {band.title()}")
	# plt.show()
	plt.savefig(os.path.join(OUTPUT_FOLDER, 'plot.png'), bbox_inches='tight')


# show_graph(counted_words, 10, "Gojira")