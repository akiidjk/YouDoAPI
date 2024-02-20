from datetime import datetime
from uuid import UUID
from model.pomodoro import Pomodoro
from repository.pomodoro import PomodoroRepository
from schema import PomodoroInput, PomodoroType


class PomodoroService:
    """Service class for the pomodoro entity. This class is responsible to manage all operations related with pomodoros in.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def create(pomodoro_data: PomodoroInput):
        """Create a new pomodoro in the database.

        Args:
            pomodoro_data (PomodoroInput): _description_
        """
        pomodoro = Pomodoro()
        pomodoro.date_time = pomodoro_data.date_time
        pomodoro.user_id = pomodoro_data.user_id
        pomodoro.duration = pomodoro_data.duration

        await PomodoroRepository.create(pomodoro)
        return PomodoroType(id=pomodoro.id,
                            date_time=pomodoro.date_time,
                            duration=pomodoro.duration,
                            user_id=pomodoro.user_id)

    @staticmethod
    async def delete(pomodoro_id: UUID) -> UUID:
        """Method to remove a specific pomodoro from the database.

        Args:
            pomodoro_id (UUID): _description_
        """
        await PomodoroRepository.delete(pomodoro_id)
        return pomodoro_id

    @staticmethod
    async def update(pomodoro_id: UUID, pomodoro_data: PomodoroInput) -> str:
        """Method to update an existing pomodoro entry in the DB.

        Args:
            pomodoro_id (UUID): _description_
            pomodoro_data (_type_): _description_

        Returns:
            _type_: _description_
        """
        pomodoro = Pomodoro()
        pomodoro.date_time = pomodoro_data.date_time
        pomodoro.duration = pomodoro_data.duration
        pomodoro.user_id = pomodoro_data.user_id

        await PomodoroRepository.update(pomodoro_id, pomodoro)
        return f'Successfully updated data by id {pomodoro_id}'


    @staticmethod
    async def get_by_id(pomodoro_id: UUID) -> PomodoroType:
        """Get an specific pomodoro by its id.

        Args:
            pomodoro_id (int): _description_

        Returns:
            _type_: _description_
        """
        pomodoro = await PomodoroRepository.get_by_id(pomodoro_id)
        return PomodoroType(id=pomodoro.id,
                            date_time=pomodoro.date_time,
                            duration=pomodoro.duration,
                            user_id=pomodoro.user_id)

    @staticmethod
    async def get_by_user(pomodoro_user: UUID) -> list[PomodoroType]:
        """Get an specific pomodoro by its id.

        Args:
            pomodoro_user (int): _description_

        Returns:
            _type_: _description_
        """
        list_pomodoro = await PomodoroRepository.get_by_user(pomodoro_user)
        return [PomodoroType(id=pomodoro.id,
                             date_time=pomodoro.date_time,
                             duration=pomodoro.duration,
                             user_id=pomodoro.user_id) for pomodoro in list_pomodoro]

    @staticmethod
    async def get_by_month(pomodoro_user: UUID, pomodoro_date: datetime) -> list[PomodoroType]:
        """Get the pomodoros by the month.

        Args:
            pomodoro_user (UUID): _description_
            pomodoro_date (datetime): _description_

        Returns:
            list[PomodoroType]: _description_
        """
        list_pomodoro = await PomodoroRepository.get_by_month(pomodoro_user, pomodoro_date)
        return [PomodoroType(id=pomodoro.id,
                             date_time=pomodoro.date_time,
                             duration=pomodoro.duration,
                             user_id=pomodoro.user_id) for pomodoro in list_pomodoro]
