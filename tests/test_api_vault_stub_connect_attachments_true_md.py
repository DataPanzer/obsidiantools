import pytest
import numpy as np
import pandas as pd
from pathlib import Path
from pandas.testing import assert_series_equal


from obsidiantools.api import Vault

# NOTE: run the tests from the project dir.
WKD = Path().cwd()


@pytest.fixture
def actual_connected_vault():
    return (Vault(WKD / 'tests/vault-stub')
            .connect(attachments=True))


@pytest.fixture
def expected_note_metadata_dict():
    return {
        'rel_filepath': {'Sussudio': Path('Sussudio.md'),
                         'Isolated note': Path('Isolated note.md'),
                         'Brevissimus moenia': Path('lipsum/Brevissimus moenia.md'),
                         'Ne fuit': Path('lipsum/Ne fuit.md'),
                         'Alimenta': Path('lipsum/Alimenta.md'),
                         'Vulnera ubera': Path('lipsum/Vulnera ubera.md'),
                         'lipsum/Isolated note': Path('lipsum/Isolated note.md'),
                         'Causam mihi': Path('lipsum/Causam mihi.md'),
                         'American Psycho (film)': np.NaN,
                         'Tarpeia': np.NaN,
                         'Caelum': np.NaN,
                         'Vita': np.NaN,
                         'Aras Teucras': np.NaN,
                         'Manus': np.NaN,
                         'Bacchus': np.NaN,
                         'Amor': np.NaN,
                         'Virtus': np.NaN,
                         'Tydides': np.NaN,
                         'Dives': np.NaN,
                         'Aetna': np.NaN},
        # abs_filepath would be here
        'note_exists': {'Sussudio': True,
                        'Isolated note': True,
                        'Brevissimus moenia': True,
                        'Ne fuit': True,
                        'Alimenta': True,
                        'Vulnera ubera': True,
                        'lipsum/Isolated note': True,
                        'Causam mihi': True,
                        'American Psycho (film)': False,
                        'Tarpeia': False,
                        'Caelum': False,
                        'Vita': False,
                        'Aras Teucras': False,
                        'Manus': False,
                        'Bacchus': False,
                        'Amor': False,
                        'Virtus': False,
                        'Tydides': False,
                        'Dives': False,
                        'Aetna': False},
        'n_backlinks': {'Sussudio': 0,
                        'Isolated note': 0,
                        'Brevissimus moenia': 1,
                        'Ne fuit': 2,
                        'Alimenta': 0,
                        'Vulnera ubera': 0,
                        'lipsum/Isolated note': 0,
                        'Causam mihi': 1,
                        'American Psycho (film)': 1,
                        'Tarpeia': 3,
                        'Caelum': 3,
                        'Vita': 3,
                        'Aras Teucras': 1,
                        'Manus': 3,
                        'Bacchus': 5,
                        'Amor': 2,
                        'Virtus': 1,
                        'Tydides': 1,
                        'Dives': 1,
                        'Aetna': 1},
        'n_wikilinks': {'Sussudio': 1.0,
                        'Isolated note': 0.0,
                        'Brevissimus moenia': 3.0,
                        'Ne fuit': 6.0,
                        'Alimenta': 12.0,
                        'Vulnera ubera': 3.0,
                        'lipsum/Isolated note': 0.0,
                        'Causam mihi': 4.0,
                        'American Psycho (film)': np.NaN,
                        'Tarpeia': np.NaN,
                        'Caelum': np.NaN,
                        'Vita': np.NaN,
                        'Aras Teucras': np.NaN,
                        'Manus': np.NaN,
                        'Bacchus': np.NaN,
                        'Amor': np.NaN,
                        'Virtus': np.NaN,
                        'Tydides': np.NaN,
                        'Dives': np.NaN,
                        'Aetna': np.NaN},
        'n_tags': {'Sussudio': 5.0,
                   'Isolated note': 0.0,
                   'Brevissimus moenia': 0.0,
                   'Ne fuit': 0.0,
                   'Alimenta': 0.0,
                   'Vulnera ubera': 0.0,
                   'lipsum/Isolated note': 0.0,
                   'Causam mihi': 0.0,
                   'American Psycho (film)': np.NaN,
                   'Tarpeia': np.NaN,
                   'Caelum': np.NaN,
                   'Vita': np.NaN,
                   'Aras Teucras': np.NaN,
                   'Manus': np.NaN,
                   'Bacchus': np.NaN,
                   'Amor': np.NaN,
                   'Virtus': np.NaN,
                   'Tydides': np.NaN,
                   'Dives': np.NaN,
                   'Aetna': np.NaN},
        'n_embedded_files': {'Isolated note': 0.0,
                             'Sussudio': 2.0,
                             'Brevissimus moenia': 0.0,
                             'Ne fuit': 0.0,
                             'Alimenta': 0.0,
                             'Vulnera ubera': 0.0,
                             'lipsum/Isolated note': 0.0,
                             'Causam mihi': 0.0,
                             'American Psycho (film)': np.NaN,
                             'Tarpeia': np.NaN,
                             'Caelum': np.NaN,
                             'Vita': np.NaN,
                             'Aras Teucras': np.NaN,
                             'Manus': np.NaN,
                             'Bacchus': np.NaN,
                             'Amor': np.NaN,
                             'Virtus': np.NaN,
                             'Tydides': np.NaN,
                             'Dives': np.NaN,
                             'Aetna': np.NaN}
    }


@pytest.fixture
def expected_media_file_metadata_dict():
    return {
        'rel_filepath': {'1999.flac': np.NaN,
                         'Sussudio.mp3': np.NaN},
        # abs_filepath would be here
        'file_exists': {'1999.flac': False,
                        'Sussudio.mp3': False},
        'n_backlinks': {'1999.flac': 1,
                        'Sussudio.mp3': 1},
    }


@pytest.fixture
def expected_embedded_files_index():
    return {'Isolated note': [],
            'lipsum/Isolated note': [],
            'Sussudio': ['Sussudio.mp3', '1999.flac'],
            'Brevissimus moenia': [],
            'Ne fuit': [],
            'Alimenta': [],
            'Vulnera ubera': [],
            'Causam mihi': []}

@pytest.fixture
def actual_note_metadata_df(actual_connected_vault):
    return actual_connected_vault.get_note_metadata()


@pytest.fixture
def actual_media_file_metadata_df(actual_connected_vault):
    return actual_connected_vault.get_media_file_metadata()


def test_get_metadata_cols(actual_note_metadata_df):
    assert isinstance(actual_note_metadata_df, pd.DataFrame)

    expected_cols = ['rel_filepath', 'abs_filepath',
                     'note_exists',
                     'n_backlinks', 'n_wikilinks',
                     'n_tags',
                     'n_embedded_files',
                     'modified_time']
    assert actual_note_metadata_df.columns.tolist() == expected_cols


def test_get_metadata_dtypes(actual_note_metadata_df):
    assert actual_note_metadata_df['rel_filepath'].dtype == 'object'
    assert actual_note_metadata_df['abs_filepath'].dtype == 'object'
    assert actual_note_metadata_df['note_exists'].dtype == 'bool'
    assert actual_note_metadata_df['n_backlinks'].dtype == 'int'
    assert actual_note_metadata_df['n_wikilinks'].dtype == 'float'
    assert actual_note_metadata_df['n_tags'].dtype == 'float'
    assert actual_note_metadata_df['n_embedded_files'].dtype == 'float'
    assert actual_note_metadata_df['modified_time'].dtype == 'datetime64[ns]'


def test_get_metadata_backlinks(actual_note_metadata_df,
                                expected_note_metadata_dict):
    TEST_COL = 'n_backlinks'

    actual_series = actual_note_metadata_df[TEST_COL]
    expected_series = (pd.Series(expected_note_metadata_dict.get(TEST_COL),
                                 name=TEST_COL)
                       .rename_axis('note'))
    assert_series_equal(actual_series, expected_series,
                        check_like=True)


def test_backlink_and_wikilink_totals_not_equal_for_test_vault(actual_note_metadata_df):
    # every wikilink is another note's backlink
    # INEQUALITY is expected when canvas files are INCLUDED in wikilinks list
    # for this vault
    assert (actual_note_metadata_df['n_backlinks'].sum()
            != actual_note_metadata_df['n_wikilinks'].sum())


def test_backlink_counts(actual_connected_vault):
    expected_bl_count_subset = {
        'Sussudio': {},
        'Alimenta': {},
        'Tarpeia': {'Brevissimus moenia': 1,
                    'Alimenta': 1,
                    'Vulnera ubera': 1},
        'Ne fuit': {'Alimenta': 1,
                    'Causam mihi': 1},
        'Bacchus': {'Ne fuit': 1,
                    'Alimenta': 4},
        '1999.flac': {'Sussudio': 1},
        'Sussudio.mp3': {'Sussudio': 1}
    }

    for k in list(expected_bl_count_subset.keys()):
        assert (actual_connected_vault.get_backlink_counts(k)
                == expected_bl_count_subset.get(k))

    with pytest.raises(ValueError):
        actual_connected_vault.get_backlink_counts("Note that isn't in vault at all")


def test_nonexistent_media_files(actual_connected_vault, actual_media_file_metadata_df):
    expected_non_e_files = ['1999.flac', 'Sussudio.mp3']

    assert isinstance(actual_connected_vault.nonexistent_media_files, list)

    assert (set(actual_connected_vault.nonexistent_media_files)
            == set(expected_non_e_files))
    assert (set(actual_media_file_metadata_df.loc[~actual_media_file_metadata_df['file_exists'], :]
                .index.tolist())
            == set(expected_non_e_files))


def test_isolated_notes(actual_connected_vault):
    expected_isol_notes = ['Isolated note', 'lipsum/Isolated note']

    assert isinstance(actual_connected_vault.isolated_notes, list)

    assert (set(actual_connected_vault.isolated_notes)
            == set(expected_isol_notes))

    # isolated notes can't have backlinks
    for n in actual_connected_vault.isolated_notes:
        assert actual_connected_vault.get_backlink_counts(n) == {}
    # isolated notes can't have wikilinks
    for n in actual_connected_vault.isolated_notes:
        assert actual_connected_vault.get_wikilinks(n) == []


def test_isolated_canvas_files(actual_connected_vault):
    expected_isol_files = ['Crazy wall.canvas']

    assert isinstance(actual_connected_vault.isolated_canvas_files, list)

    assert (set(actual_connected_vault.isolated_canvas_files)
            == set(expected_isol_files))
