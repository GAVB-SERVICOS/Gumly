import numpy as np
import pandas as pd
from librosa import feature, load

class EmbeddingAudio(object):
    
    def __init__(self):        
        
        self.features = [
            ('chroma_stft', feature.chroma_stft),
            ('rms', feature.rms),
            ('spectral_centroid', feature.spectral_centroid),
            ('spectral_bandwidth', feature.spectral_bandwidth),
            ('spectral_rolloff', feature.spectral_rolloff),
            ('zero_crossing_rate', feature.zero_crossing_rate),
            ('mfcc', feature.mfcc)
        ]
    
    def create_feature_pandas(self, data_dir_target=None, df_save_embedding=None, sr=22050):
        
        ## Lendo DataFrame
        if type(data_dir_target) == str:
            df = pd.read_csv(data_dir_target)
        elif type(data_dir_target) == type(pd.DataFrame()):
            df = data_dir_target.copy()
        else:
            return 'Erro'

        path_sound = df['path_sound'].values        
        target = df['target'].values        
        
        ## Criando o dicionário do embedding
        header = 'filename chroma_stft rms spectral_centroid spectral_bandwidth spectral_rolloff zero_crossing_rate'
        for i in range(1,21):
            header += f' mfcc_{i}'
        header += ' target'
        data = {h:[] for h in header.split()}             
        
        ## Obtendo o emdeding
        for path, label in zip(path_sound, target):
            try:
                y, _ = load(path, sr=sr)
                for name, func in self.features:
                
                    if name in ['rms', 'zero_crossing_rate']:
                        y0 = func(y=y)
                        data[name].append(np.mean(y0))
                
                    elif name == 'mfcc':
                        y0 = func(y=y, sr=sr)
                        for i, m in enumerate(y0, 1):
                            data[f'{name}_{i}'].append(np.mean(m))
                
                    else:
                        y0 = func(y=y, sr=sr)
                        data[name].append(np.mean(y0)) 
                
                data['filename'].append(path)               
                data['target'].append(label)     

            except Exception as e:
                print(e)        

        # DataFrame
        data_sound = pd.DataFrame(data=data)

        if df_save_embedding:
            data_sound.to_csv(df_save_embedding, index=False)

        return data_sound
    
    def create_feature(self, audio, sr=22050):
        
        features_segmentation = []

        ## Obtendo o emdeding
        for y in audio:
            feature_segmentation = []
            try:
                for name, func in self.features:
                    if name in ['rms', 'zero_crossing_rate']:
                        y0 = func(y=y)
                        feature_segmentation.append(np.mean(y0))
                
                    elif name == 'mfcc':
                        y0 = func(y=y, sr=sr)
                        for i, m in enumerate(y0, 1):
                            feature_segmentation.append(np.mean(m))
                
                    else:
                        y0 = func(y=y, sr=sr)
                        feature_segmentation.append(np.mean(y0))     

            except Exception as e:
                print(e)        

            features_segmentation.append(feature_segmentation)
        
        features_segmentation = np.array(features_segmentation)
        return features_segmentation
    
    def reshape_sound_and_target(self, sound_list, targets_list, sr, segment_size_t=1.0):
        """        
        Parameters:
        sound_list, 
        targets_list, 
        segment_size_t: segment size in seconds
        """
        segments_sound, segments_target = [], []
        
        if type(sound_list) == type([]):
            if len(sound_list) == 1:
                sound_list = [sound_list]
        elif type(sound_list) == type(np.array([1])):
            if type(sound_list[0]) not in [type(np.array([1])), type([])]:
                sound_list = [sound_list]
        
        range_ = range(len(sound_list))
        
        if type(sr) in [type(1), type(1.0)]:
            sr = [sr for _ in range_]
        elif len(sr) != len(sound_list):
            sr = [sr[0] for _ in range_]
        
        for i in range_:
            
            y = sound_list[i]
            # Signal size
            signal_len = len(y) 
            # segment size in samples
            segment_size = int(segment_size_t * sr[i])  
            # Break signal into list of segments in a single-line Python code
            segments = [
                y[x:x + segment_size] for x in np.arange(0, signal_len, segment_size)
            ]
            # Reshaping the target list according to the segmented audio 
            target = [targets_list[i] for _ in range(len(segments))]

            segments_sound.extend(segments)
            segments_target.extend(target)

        segments_sound = np.array(segments_sound)
        segments_target = np.array(segments_target)
        
        return segments_sound, segments_target

