from isort import file
import numpy as np
import pandas as pd
import pytest
from numpy.testing import assert_almost_equal

import librosa

from gumly.embedding_audio import EmbeddingAudio

def test_feature_engineering_split_features_and_target():    
    data = {'path_sound':[], 'target':[]}
    for arq in ['choice', 'brahms']:
        filename = librosa.example(arq)
        data['path_sound'].append(filename)
        data['target'].append('target')
    
    df = pd.DataFrame(data)
    
    embedding = EmbeddingAudio()
    df_embedding = embedding.create_feature_pandas(data_dir_target=df)

    assert type(df_embedding) == type(pd.DataFrame())
    assert df_embedding.shape[0] == 2
    assert df_embedding.shape[1] == 28

def test_shape_numpy_array():  
    
    audio_list = []
    for arq in ['choice', 'brahms']:
        filename = librosa.example(arq)
        audio, _ = librosa.load(filename)
        audio_list.append(audio)

    embedding = EmbeddingAudio()
    audio_embedding = embedding.create_feature(audio=audio_list, sr=22050)

    assert audio_embedding.shape[0] == 2
    assert audio_embedding.shape[1] == 26

def test_reshape_sound_and_target():
    count_segments = 0    
    segment_size_t = 0.5
    targets = ['choice', 'brahms', 'fishin']    
    
    filename_list = []
    for target in targets:
        filename = librosa.example(target)
        filename_list.append(filename)

        audio, sr = librosa.load(filename)
        count_segments += np.ceil((audio.shape[0] / sr)/segment_size_t)

    embedding = EmbeddingAudio()
    segments_sound, segments_target, sr = embedding.reshape_sound_and_target(
        path_sound = filename_list,
        targets = targets,
        segment_size_t = segment_size_t
    )

    assert segments_sound.shape[0] == count_segments
    assert segments_target.shape[0] == count_segments
    assert np.unique(segments_target).shape[0] == len(targets)