"""A tiny fake chat model for testing an agent without calling a real LLM.

`ScriptedChatModel` returns the messages in `responses` one by one. Use it to
demo error handling (for example, a tool call for a city that is not in the
database) without paying for API calls.
"""

from __future__ import annotations

import itertools
from typing import Callable

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from pydantic import PrivateAttr


class ScriptedChatModel(BaseChatModel):
    """Fake chat model that plays back a scripted list of responses.

    Each item in ``responses`` is either an ``AIMessage`` or a function
    ``(messages) -> AIMessage``. When the list is exhausted, the last item is
    repeated. Incoming requests are stored in ``received``; tools from
    ``bind_tools`` are stored in ``bound_tools``.
    """

    responses: list
    _index: int = PrivateAttr(default=0)
    _received: list = PrivateAttr(default_factory=list)
    _bound_tools: list = PrivateAttr(default_factory=list)

    @property
    def _llm_type(self) -> str:
        return "scripted"

    @property
    def received(self) -> list[list[BaseMessage]]:
        return self._received

    @property
    def bound_tools(self) -> list:
        return self._bound_tools

    def bind_tools(self, tools, **kwargs):  # noqa: D401 — LangChain signature
        self._bound_tools = list(tools)
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs) -> ChatResult:
        self._received.append(list(messages))
        item = self.responses[min(self._index, len(self.responses) - 1)]
        self._index += 1
        message = item(messages) if callable(item) else item
        message = message.model_copy(deep=True)
        return ChatResult(generations=[ChatGeneration(message=message)])


_call_ids = itertools.count(1)


def tool_call(name: str, **args) -> AIMessage:
    """An ``AIMessage`` that contains a single tool call ``name(**args)``."""
    return AIMessage(
        content="",
        tool_calls=[{"name": name, "args": args, "id": f"call_{next(_call_ids)}"}],
    )


def endless_tool_calls(name: str, **args) -> Callable[[list], AIMessage]:
    """Response function: the model keeps calling the same tool."""
    return lambda messages: tool_call(name, **args)
