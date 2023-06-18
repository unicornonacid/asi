import numpy as np

import pandas as pd

from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset
from evidently.test_preset import DataQualityTestPreset


data_stability = TestSuite(tests=[
    DataStabilityTestPreset(),
])

basedata=pd.read("kedro/data

