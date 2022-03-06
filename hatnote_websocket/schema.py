"""Schema for the hatnote-websocket response messages."""


import pydantic


class Message(pydantic.BaseModel):
    """Schema for the hatnote-websocket response messages."""

    action: str
    change_size: int | None
    flags: str | None
    hashtags: list[str]
    is_anon: bool
    is_bot: bool
    is_minor: bool
    is_new: bool
    is_patrolled: bool | None
    mentions: list[str]
    ns: str
    page_title: str
    parsed_summary: str | None
    section: str
    summary: str | None
    user: str
