from abc import ABC, abstractmethod
from typing import Dict


class UserFinder(ABC):
    @abstractmethod
    def find_user(self, user_id: str) -> Dict:
        pass