from __future__ import annotations

from typing import Any

import optuna
from optuna.distributions import BaseDistribution


class DeterministicSampler(optuna.samplers.BaseSampler):
    def __init__(self, params: dict[str, Any]) -> None:
        self.params = params

    def infer_relative_search_space(
        self, study: "optuna.study.Study", trial: "optuna.trial.FrozenTrial"
    ) -> dict[str, BaseDistribution]:
        return {}

    def sample_relative(
        self,
        study: "optuna.study.Study",
        trial: "optuna.trial.FrozenTrial",
        search_space: dict[str, BaseDistribution],
    ) -> dict[str, Any]:
        return {}

    def sample_independent(
        self,
        study: "optuna.study.Study",
        trial: "optuna.trial.FrozenTrial",
        param_name: str,
        param_distribution: BaseDistribution,
    ) -> Any:
        param_value = self.params[param_name]
        assert param_distribution._contains(param_distribution.to_internal_repr(param_value))
        return param_value
