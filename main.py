from marvel.marvel import Marvel
from keys import private_key, public_key
import json

base_file_name = 'comics{0}.json'

basic_limit = 100
starting_offset = 0
number_to_bring = 200


def del_file_content():
    with open(base_file_name, 'w') as the_file:
        the_file.write("")


def main():
    m = Marvel(public_key, private_key)
    del_file_content()
    for i in xrange(starting_offset, number_to_bring, basic_limit):
        comics = m.get_comics(limit=basic_limit, offset=i, )
        with open(base_file_name.format(), 'a') as the_file:
            the_file.write(json.dumps(comics.data.to_dict()['results']))


if __name__ == '__main__':
    main()
