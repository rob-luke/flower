# Copyright 2020 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower client (abstract base class)."""


from abc import ABC

from flwr.common import (
    EvaluateIns,
    EvaluateRes,
    FitIns,
    FitRes,
    GetParametersIns,
    GetParametersRes,
    GetPropertiesIns,
    GetPropertiesRes,
)


class Client(ABC):
    """Abstract base class for Flower clients."""

    def get_properties(self, ins: GetPropertiesIns) -> GetPropertiesRes:
        """Return set of client's properties.

        Parameters
        ----------
        ins : GetPropertiesIns
            The get properties instructions received from the server containing
            a dictionary of configuration values.

        Returns
        -------
        GetPropertiesRes
            The current client properties.
        """

    def get_parameters(self, ins: GetParametersIns) -> GetParametersRes:
        """Return the current local model parameters.

        Parameters
        ----------
        ins : GetParametersIns
            The get parameters instructions received from the server containing
            a dictionary of configuration values.

        Returns
        -------
        GetParametersRes
            The current local model parameters.
        """

    def fit(self, ins: FitIns) -> FitRes:
        """Refine the provided weights using the locally held dataset.

        Parameters
        ----------
        ins : FitIns
            The training instructions containing (global) model parameters
            received from the server and a dictionary of configuration values
            used to customize the local training process.

        Returns
        -------
        FitRes
            The training result containing updated parameters and other details
            such as the number of local training examples used for training.
        """

    def evaluate(self, ins: EvaluateIns) -> EvaluateRes:
        """Evaluate the provided weights using the locally held dataset.

        Parameters
        ----------
        ins : EvaluateIns
            The evaluation instructions containing (global) model parameters
            received from the server and a dictionary of configuration values
            used to customize the local evaluation process.

        Returns
        -------
        EvaluateRes
            The evaluation result containing the loss on the local dataset and
            other details such as the number of local data examples used for
            evaluation.
        """


def has_get_properties(client: Client) -> bool:
    """Check if Client implements get_properties."""
    return type(client).get_properties != Client.get_properties


def has_get_parameters(client: Client) -> bool:
    """Check if Client implements get_parameters."""
    return type(client).get_parameters != Client.get_parameters


def has_fit(client: Client) -> bool:
    """Check if Client implements fit."""
    return type(client).fit != Client.fit


def has_evaluate(client: Client) -> bool:
    """Check if Client implements evaluate."""
    return type(client).evaluate != Client.evaluate
