from typing import Optional

from langchain_core.language_models.chat_models import BaseChatModel
from megaparse.formatter.structured_formatter import StructuredFormatter
from pydantic import BaseModel


class CustomStructuredFormatter(StructuredFormatter):
    async def format_string(
        self,
        text: str,
        file_path: str | None = None,
    ) -> str:
        """
        Structure the file using an AI language model.
        Args:
            text: The text to format.
            file_path: The file path of the text.
            model: The AI language model to use for formatting.
        Returns:
            The structured text.
        """
        if not self.model:
            raise ValueError("A Model is needed to use the CustomStructuredFormatter.")
        print("Formatting text using CustomStructuredFormatter...")
        if len(text) < 0:
            raise ValueError(
                "A non empty text is needed to format text using CustomStructuredFormatter."
            )
        if not self.output_model:
            raise ValueError(
                "An output model is needed to structure text using CustomStructuredFormatter."
            )

        structured_model = self.model.with_structured_output(self.output_model)  # type: ignore

        formatted_text = structured_model.invoke(
            f"Parse the text in a structured format: {text}"
        )
        assert isinstance(formatted_text, BaseModel), "Model output is not a BaseModel."

        return formatted_text.model_dump_json()
