import dictogram


def open_file_return_list(self, sample_text):
    with open(sample_text, 'r') as phile:
        data = list(phile.readlines())
        # data = phile.read().split()

        return data
