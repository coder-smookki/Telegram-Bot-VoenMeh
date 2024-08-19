from enum import Enum


class SlashCommand(str, Enum):
    """Слэш команды бота."""

    START = "start"
    HELP = "help"
    MENU = "menu"
    CANCEL = "cancel"
    STOP = "stop"

class TextCommand(str, Enum):
    """Текстовые команды бота."""

    START = "Старт"
    HELP = "Помощь"
    MENU = "Меню"
    ADMIN_PANEL = "❗Админ панель"
    CANCEL = "Отмена"
    STOP = CANCEL

class BotMenu(str, Enum):
    """Callback'и для менюшек бота."""

    MAIN_MENU = "main_menu"

class RoleEnum(str, Enum):
    """Роли (права доступа) пользователей."""

    SUPERADMIN = "superadmin"
    ADMIN = "admin"

    @staticmethod
    def all_roles() -> list[str]:
        """Все роли."""
        return [role.value if isinstance(role, Enum) else role for role in RoleEnum]

    @staticmethod
    def roles_which_can_be_edited() -> list[str]:
        """Роли, которые можно редактировать юзерам."""
        return [
            role.value if isinstance(role, Enum) else role
            for role in RoleEnum
            if role != RoleEnum.SUPERADMIN
        ]