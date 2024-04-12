import abc
from users.model.user_model import User
class UserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, name: str, email: str)-> User:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, id:int) -> User:
        raise NotImplementedError

class LocalUserRepository(UserRepository):
    
    def __init__(self):
        self.users = []

    def add(self, name: str, email: str) -> User:
        user = User(
        id=len(self.users) + 1,
        name=name,
        email=email
    )
        self.users.append(user)
        return user
    
    def get(self, id:int) -> User:
        user_found = None
        for user in self.users:
            if user.id == id:
                user_found = user
                break
        return user_found