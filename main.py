from marvel.marvel import Marvel
from keys import private_key, public_key
import json
from tqdm import tqdm
from conf import *
from path_utils import prep_data_dir


def main():
    m = Marvel(public_key, private_key)
    prep_data_dir(folder)
    for idx, current_offset in enumerate(tqdm(xrange(starting_offset, total_number_to_bring, basic_limit))):
        comics = m.get_comics(limit=basic_limit, offset=current_offset, )
        with open(base_file_name.format(folder, idx), 'a') as the_file:
            the_file.write(json.dumps(comics.data.to_dict()['results']))


if __name__ == '__main__':
    main()
