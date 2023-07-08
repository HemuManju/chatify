from typing import Any, List, Mapping, Optional


import random
import requests as req
import os


from langchain.llms.base import LLM


class FakeListLLM(LLM):
    """Fake LLM wrapper for testing purposes.

    Attributes
    ----------
    responses : List
        List of responses.
    """

    responses: List

    @property
    def _llm_type(self) -> str:
        """Return type of LLM.

        Returns
        -------
        str
            Type of LLM.
        """
        return "fake-list"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """First try to lookup in queries, else return 'foo' or 'bar'.

        Parameters
        ----------
        prompt : str
            Input prompt.
        stop : List[str], optional
            List of stop tokens, by default None.

        Returns
        -------
        str
            Generated response.
        """
        response = self.responses[random.randint(0, len(self.responses) - 1)]
        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters.

        Returns
        -------
        Mapping[str, Any]
            Identifying parameters.
        """
        return {}


def download_cache_database(config):
    try:
        cache_db_version = config['cache_db_version']
        file_name = f'NMA_2023_v{cache_db_version}.cache'
        url = config['url']
        res = req.get(url)
        with open(os.path.join(os.getcwd(), file_name), 'wb') as f:
            f.write(res.content)
            f.close()
    except FileNotFoundError:
        print(f'{file_name} could not be downloaded from the provided cache URL: {url}')
