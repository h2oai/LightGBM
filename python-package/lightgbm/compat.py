# coding: utf-8
"""Compatibility library."""

"""pandas"""
try:
    from pandas import DataFrame as pd_DataFrame
    from pandas import Series as pd_Series
    from pandas import concat
    try:
        from pandas import CategoricalDtype as pd_CategoricalDtype
    except ImportError:
        from pandas.api.types import CategoricalDtype as pd_CategoricalDtype
    PANDAS_INSTALLED = True
except ImportError:
    PANDAS_INSTALLED = False

    class pd_Series:  # type: ignore
        """Dummy class for pandas.Series."""

        def __init__(self, *args, **kwargs):
            pass

    class pd_DataFrame:  # type: ignore
        """Dummy class for pandas.DataFrame."""

        def __init__(self, *args, **kwargs):
            pass

    class pd_CategoricalDtype:  # type: ignore
        """Dummy class for pandas.CategoricalDtype."""

        def __init__(self, *args, **kwargs):
            pass

    concat = None

"""matplotlib"""
try:
    import matplotlib
    MATPLOTLIB_INSTALLED = True
except ImportError:
    MATPLOTLIB_INSTALLED = False

"""graphviz"""
try:
    import graphviz
    GRAPHVIZ_INSTALLED = True
except ImportError:
    GRAPHVIZ_INSTALLED = False

"""datatable"""
try:
    import datatable
    if hasattr(datatable, "Frame"):
        dt_DataTable = datatable.Frame
    else:
        dt_DataTable = datatable.DataTable
    DATATABLE_INSTALLED = True
except ImportError:
    DATATABLE_INSTALLED = False

    class dt_DataTable:  # type: ignore
        """Dummy class for datatable.DataTable."""

        def __init__(self, *args, **kwargs):
            pass


"""sklearn"""
try:
    from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
    from sklearn.preprocessing import LabelEncoder
    from sklearn.utils.class_weight import compute_sample_weight
    from sklearn.utils.multiclass import check_classification_targets
    from sklearn.utils.validation import assert_all_finite, check_array, check_X_y
    try:
        from sklearn.exceptions import NotFittedError
        from sklearn.model_selection import GroupKFold, StratifiedKFold
    except ImportError:
        from sklearn.cross_validation import GroupKFold, StratifiedKFold
        from sklearn.utils.validation import NotFittedError
    try:
        from sklearn.utils.validation import _check_sample_weight
    except ImportError:
        from sklearn.utils.validation import check_consistent_length

        # dummy function to support older version of scikit-learn
        def _check_sample_weight(sample_weight, X, dtype=None):
            check_consistent_length(sample_weight, X)
            return sample_weight

    SKLEARN_INSTALLED = True
    _LGBMModelBase = BaseEstimator
    _LGBMRegressorBase = RegressorMixin
    _LGBMClassifierBase = ClassifierMixin
    _LGBMLabelEncoder = LabelEncoder
    LGBMNotFittedError = NotFittedError
    _LGBMStratifiedKFold = StratifiedKFold
    _LGBMGroupKFold = GroupKFold
    _LGBMCheckXY = check_X_y
    _LGBMCheckArray = check_array
    _LGBMCheckSampleWeight = _check_sample_weight
    _LGBMAssertAllFinite = assert_all_finite
    _LGBMCheckClassificationTargets = check_classification_targets
    _LGBMComputeSampleWeight = compute_sample_weight
except ImportError:
    SKLEARN_INSTALLED = False

    class _LGBMModelBase:  # type: ignore
        """Dummy class for sklearn.base.BaseEstimator."""

        pass

    class _LGBMClassifierBase:  # type: ignore
        """Dummy class for sklearn.base.ClassifierMixin."""

        pass

    class _LGBMRegressorBase:  # type: ignore
        """Dummy class for sklearn.base.RegressorMixin."""

        pass

    _LGBMLabelEncoder = None
    LGBMNotFittedError = ValueError
    _LGBMStratifiedKFold = None
    _LGBMGroupKFold = None
    _LGBMCheckXY = None
    _LGBMCheckArray = None
    _LGBMCheckSampleWeight = None
    _LGBMAssertAllFinite = None
    _LGBMCheckClassificationTargets = None
    _LGBMComputeSampleWeight = None

"""dask"""
try:
    import pkg_resources
    pkg_resources.get_distribution('dask')
    DASK_INSTALLED = True
except pkg_resources.DistributionNotFound:
    DASK_INSTALLED = False
