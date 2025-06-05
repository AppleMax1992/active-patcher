from active_patcher.version import __version__

# this is the only file in this project where star imports are allowed
from active_patcher import (
    classifiers,
    data,
    initialization,
    integrations,
    query_strategies,
    stopping_criteria,
    training,
    utils
)

from active_patcher.classifiers import *
from active_patcher.data import *
from active_patcher.initialization import *
from active_patcher.integrations import *
from active_patcher.query_strategies import *
from active_patcher.stopping_criteria import *
from active_patcher.training import *
from active_patcher.utils import *

from active_patcher.active_learner import (
    ActiveLearner,
    AbstractPoolBasedActiveLearner,
    PoolBasedActiveLearner
)
from active_patcher.base import (
    LABEL_UNLABELED,
    LABEL_IGNORED,
    OPTIONAL_DEPENDENCIES,
    check_optional_dependency
)
from active_patcher.exceptions import (
    ActiveLearnerException,
    ConstraintViolationError,
    LearnerNotInitializedException,
    MissingOptionalDependencyError
)
from active_patcher.version import get_version
from active_patcher.utils.system import is_pytorch_available, is_transformers_available

__all__ = (
    classifiers.__all__ +
    data.__all__ +
    initialization.__all__ +
    query_strategies.__all__ +
    stopping_criteria.__all__ +
    training.__all__ +
    utils.__all__
)


__all__ = __all__ + [
    'ActiveLearner',
    'AbstractPoolBasedActiveLearner',
    'PoolBasedActiveLearner',
    'LABEL_UNLABELED',
    'LABEL_IGNORED',
    'OPTIONAL_DEPENDENCIES',
    'check_optional_dependency',
    'ActiveLearnerException',
    'ConstraintViolationError',
    'LearnerNotInitializedException',
    'MissingOptionalDependencyError',
    'get_version'
]


if is_pytorch_available():
    from active_patcher.integrations.pytorch import *

    __all__ = __all__ + integrations.pytorch.__all__

if is_transformers_available():
    from active_patcher.integrations.transformers import *

    __all__ = __all__ + integrations.transformers.__all__
