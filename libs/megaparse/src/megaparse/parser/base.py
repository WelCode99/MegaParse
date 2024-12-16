from abc import ABC, abstractmethod
from pathlib import Path
from typing import IO

from megaparse_sdk.schema.extensions import FileExtension


class BaseParser(ABC):
    """Mother Class for all the parsers [Unstructured, LlamaParse, MegaParseVision]"""

    supported_extensions = []

    def check_supported_extension(
        self, file_extension: FileExtension | None, file_path: str | Path | None = None
    ):
        if not file_extension and not file_path:
            raise ValueError(
                "Either file_path or file_extension must be provided for UnstructuredParser"
            )
        if file_path and not file_extension:
            file_path = Path(file_path) if isinstance(file_path, str) else file_path
            file_extension = FileExtension(file_path.suffix)
        if file_extension not in self.supported_extensions:
            raise ValueError(
                f"Unsupported file extension {file_extension.value} for UnstructuredParser"
            )

    @abstractmethod
    async def aconvert(
        self,
        file_path: str | Path | None = None,
        file: IO[bytes] | None = None,
        file_extension: FileExtension | None = None,
        **kwargs,
    ) -> str:
        """
        Convert the given file to a specific format.

        Args:
            file_path (str | Path): The path to the file to be converted.
            **kwargs: Additional keyword arguments for the conversion process.

        Returns:
            str: The result of the conversion process.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def convert(
        self,
        file_path: str | Path | None = None,
        file: IO[bytes] | None = None,
        file_extension: FileExtension | None = None,
        **kwargs,
    ) -> str:
        """
        Convert the given file to a specific format.

        Args:
            file_path (str | Path): The path to the file to be converted.
            **kwargs: Additional keyword arguments for the conversion process.

        Returns:
            str: The result of the conversion process.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")
