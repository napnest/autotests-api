from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client



class Exercise(TypedDict):
    """
    Типизированный словарь для задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExerciseCreateData(TypedDict):
    """
    Типизированный словарь для данных создания задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExerciseUpdateData(TypedDict):
    """
    Типизированный словарь для данных обновления задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise

class ExercisesClient(APIClient):
    """
    API клиент для работы с эндпоинтом заданий (/api/v1/exercises).
    """

    def get_exercises_api(self, course_id: str) -> Response:
        """
        Получает список заданий для определенного курса.

        :param course_id: Идентификатор курса, для которого нужно получить задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises", params=course_id)

    def create_exercise_api(self, exercise_data: ExerciseCreateData) -> Response:
        """
        Создает новое задание.

        :param exercise_data: Словарь с данными title, courseId, maxScore, minScore,
        orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=exercise_data)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает информацию о конкретном задании по его идентификатору.

        :param exercise_id: Уникальный идентификатор задания

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(
            self,
            exercise_id: str,
            update_data: ExerciseUpdateData
    ) -> Response:
        """
        Обновляет данные существующего задания.

        :param exercise_id: Уникальный идентификатор обновляемого задания
        :param update_data: Словарь с данными для обновления.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=update_data)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.
        :param exercise_id: Уникальный идентификатор удаляемого задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # Реализация метода get_exercise_api
    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    # Реализация метода get_exercises_api
    def get_exercises(self, course_id: str) -> GetExercisesResponseDict:
        response = self.get_exercises_api(course_id)
        return response.json()

    # Реализация метода create_exercise
    def create_exercise(self, exercise_data: ExerciseCreateData) -> GetExercisesResponseDict:
        response = self.create_exercise_api(exercise_data)
        return response.json()

    # Реализация метода update_exercise
    def update_exercise(self, exercise_id: str,
                        update_data: ExerciseUpdateData) -> GetExercisesResponseDict:
        response = self.update_exercise_api(exercise_id, update_data)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
