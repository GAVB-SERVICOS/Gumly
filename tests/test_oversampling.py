from sklearn.datasets import make_classification
from collections import Counter
from gumly.oversampling import oversampler


def create_dataset(
    n_samples=1000,
    weights=(0.01, 0.01, 0.98),
    n_classes=3,
    class_sep=0.8,
    n_clusters=1,
):
    return make_classification(
        n_samples=n_samples,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=n_classes,
        n_clusters_per_class=n_clusters,
        weights=list(weights),
        class_sep=class_sep,
        random_state=0,
    )


def dataset_sampels(X, y):
    return sorted([x[1] for x in Counter(y).items()])


def test_random_sample():
    X, y = create_dataset()
    class_map = dataset_sampels(X, y)
    total_examples = sum(class_map)
    actual_examples = class_map[-1] * 3

    assert total_examples != actual_examples

    X_resample, y_resample = oversampler(X, y, 'random', random_state=0)
    class_map = dataset_sampels(X_resample, y_resample)
    total_examples = sum(class_map)
    actual_examples = class_map[-1] * 3

    assert total_examples == actual_examples # (10,10,100) (100,100,100)