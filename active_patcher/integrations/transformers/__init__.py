from active_patcher.integrations.pytorch.exceptions import PytorchNotFoundError

try:
    from active_patcher.integrations.transformers.classifiers.base import ModelLoadingStrategy
    from active_patcher.integrations.transformers.classifiers.classification import (
        transformers_collate_fn,
        FineTuningArguments,
        TransformerModelArguments,
        TransformerBasedClassification,
        TransformerBasedEmbeddingMixin
    )
    from active_patcher.integrations.transformers.classifiers.setfit import (
        SetFitClassification,
        SetFitModelArguments,
        SetFitClassificationEmbeddingMixin
    )
    from active_patcher.integrations.transformers.classifiers.factories import (
        SetFitClassificationFactory,
        TransformerBasedClassificationFactory
    )
    from active_patcher.integrations.transformers.datasets import (
        TransformersDataset,
        TransformersDatasetView
    )
    __all__ = [
        'ModelLoadingStrategy',
        'transformers_collate_fn',
        'FineTuningArguments',
        'TransformerModelArguments',
        'TransformerBasedClassification',
        'TransformerBasedEmbeddingMixin',
        'SetFitClassification',
        'SetFitModelArguments',
        'SetFitClassificationEmbeddingMixin',
        'TransformerBasedClassificationFactory',
        'SetFitClassificationFactory',
        'TransformersDataset',
        'TransformersDatasetView'
    ]
except PytorchNotFoundError:
    __all__ = []
