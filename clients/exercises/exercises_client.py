from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response



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
