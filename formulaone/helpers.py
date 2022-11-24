from pathlib import Path


def get_path_to_data():
    """Return path to data."""
    return Path('Data/')


def get_raw_data_path():
    """Return path to raw data."""
    return get_path_to_data() / 'RawData'


def get_tidy_data_path():
    """Return path to tidy data."""
    return get_path_to_data() / 'TidyData'
