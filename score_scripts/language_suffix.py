class LanguageSuffixHandler():
    """
    Abstract base class to handle the logic for determining file types
    based on the language.
    """
    file_type = {"python": ".py", "java": ".java", "javascript": ".js", "typescript": ".ts", "csharp": ".cs"}

    def __init__(self, language: str):
        self.language = language
    
    def get(self) -> str:
        """
        Return the file type based on the language.
        """
        return self.file_type.get(self.language, "")