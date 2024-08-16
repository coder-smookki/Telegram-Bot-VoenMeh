from datetime import date, time
import json

from redis import asyncio as aioredis
from redis.asyncio.client import Redis
from dacite import from_dict

from parser import parser
from config import (
    REDIS_HOST, REDIS_PORT,
    REDIS_EXPIRE_TIME,
    REDIS_GROUP_PREFIX, REDIS_PERIOD_KEY,
)
from exceptions import NotFoundGroupException
from dataclass import GroupData


class ScheduleRepo:
    async def _set_data(self) -> None:
        redis_client = self._get_redis_client()
        json_data = await parser()

        await redis_client.set(
            REDIS_PERIOD_KEY,
            json.dumps(json_data["Timetable"]["Period"], ensure_ascii=False),
            ex=REDIS_EXPIRE_TIME,
        )
        for group_data in json_data["Timetable"]["Group"]:
            if group_data.get("Days") is None:
                continue
            self._group_data_conversion(group_data)

            await redis_client.set(
                REDIS_GROUP_PREFIX + group_data["number"],
                json.dumps(group_data, ensure_ascii=False),
                ex=REDIS_EXPIRE_TIME,
            )


    async def get_start_date(self) -> date:
        redis_client = self._get_redis_client()
        period_data = await self._get_data(REDIS_PERIOD_KEY, redis_client)

        period_data_json = json.loads(period_data)
        return date(
            int(period_data_json["@StartYear"]),
            int(period_data_json["@StartMonth"]),
            int(period_data_json["@StartDay"]),
        )


    async def get_group_data(self, group_name: str) -> GroupData:
        """
        Args:
            group_name (str): Только верхни регистр и русские символы

        Raises:
            NotFoundGroupException: Если группа не найденна после обновления данных

        Returns: GroupData
        """
        redis_client = self._get_redis_client()

        group_data = await self._get_data(REDIS_GROUP_PREFIX + group_name, redis_client)
        group_data = json.loads(group_data)
        if group_data is None:
            raise NotFoundGroupException

        self._time_start_conversion(group_data)

        return from_dict(GroupData, group_data)


    def _time_start_conversion(self, group_data: dict):
        for day in group_data["schedule"]:
            for lesson in day["lessons"]:
                lesson["time_start"] = time.fromisoformat(lesson["time_start"])


    def _group_data_conversion(self, group_data: dict):
        self._replace_key_in_dict(group_data, "number", "@Number")
        self._replace_key_in_dict(group_data, "id", "@IdGroup")
        self._replace_key_in_dict(group_data, "schedule", "Days", "Day")

        if isinstance(group_data["schedule"], dict):
            group_data["schedule"] = [group_data["schedule"]]

        for day_schedule in group_data["schedule"]:
            self._replace_key_in_dict(day_schedule, "weekday", "@Title")
            self._replace_key_in_dict(day_schedule, "lessons", "GroupLessons", "Lesson")
            
            if isinstance(day_schedule["lessons"], dict):
                day_schedule["lessons"] = [day_schedule["lessons"]]

            for lesson in day_schedule["lessons"]:
                
                self._replace_key_in_dict(lesson, "week_code", "WeekCode")
                self._replace_key_in_dict(lesson, "discipline", "Discipline")
                self._replace_key_in_dict(lesson, "classroom", "Classroom")
                if lesson["classroom"] is None:
                    lesson["classroom"] = ""
                lesson.pop("DayTitle")
                
                self._replace_key_in_dict(lesson, "time_str", "Time")
                _time_start= lesson["time_str"].split()[0].split(":")
                lesson["time_start"] = time(int(_time_start[0]), int(_time_start[1])).isoformat()
                
                lesson["lecturers"] = list()
                if lesson.get("Lecturers") is not None:
                    
                    if isinstance(lesson["Lecturers"]["Lecturer"], dict):
                        lesson["Lecturers"]["Lecturer"] = [lesson["Lecturers"]["Lecturer"]]

                    for lecturer in lesson["Lecturers"]["Lecturer"]:
                        self._replace_key_in_dict(lecturer, "id", "IdLecturer")
                        self._replace_key_in_dict(lecturer, "short_name", "ShortName")
                        lesson["lecturers"].append(lecturer)
                    lesson.pop("Lecturers")


    def _replace_key_in_dict(self, data: dict, new_key: str, old_key: str, second_old_key: str|None=None) -> None:
        if second_old_key is None:
            data[new_key] = data[old_key]
        else:
            data[new_key] = data[old_key][second_old_key]
        data.pop(old_key)


    async def _get_data(self, key: str, redis_client: Redis) -> dict | list:
        data = await redis_client.get(key)
        if data is None:
            await self._set_data()
        return await redis_client.get(key)


    def _get_redis_client(self):
        return aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")