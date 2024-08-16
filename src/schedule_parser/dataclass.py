from dataclasses import dataclass
from datetime import time


@dataclass
class LecturerData:
    id: str
    short_name: str
    

@dataclass
class LessonData:
    week_code: str
    time_start: time
    time_str: str
    discipline: str
    lecturers: list[LecturerData]
    classroom: str


@dataclass
class DayScheduleData:
    weekday: str
    lessons: list[LessonData]


@dataclass
class GroupData:
    number: str
    id: str
    schedule: list[DayScheduleData]