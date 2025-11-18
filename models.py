from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_as_dataclass, registry 
table_registry = registry()

@mapped_as_dataclass(table_registry)
class User:
    _tablename_ = 'users'

    id: Mapped[int]
    nome_usuario: Mapped[str]
    senha: Mapped[str]
    email: Mapped[str]
    create_at: Mapped[datetime]