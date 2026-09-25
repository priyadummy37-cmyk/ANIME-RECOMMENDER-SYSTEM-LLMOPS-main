from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

from src.prompt_template import get_anime_prompt


load_dotenv()


class AnimeRecommender:
    """
    Anime recommendation service using a RAG pipeline.
    """

    def __init__(self, retriever, model_name: str):

        self.llm = ChatGroq(
            model=model_name,
            temperature=0
        )

        self.prompt = get_anime_prompt()

        # Create document chain
        self.document_chain = create_stuff_documents_chain(
            self.llm,
            self.prompt
        )

        # Create retrieval chain
        self.qa_chain = create_retrieval_chain(
            retriever,
            self.document_chain
        )

    def get_recommendation(self, query: str) -> str:
        """
        Generate anime recommendations based on the user query.

        Args:
            query: User's anime-related question.

        Returns:
            Generated anime recommendation.
        """

        result = self.qa_chain.invoke({
            "input": query
        })

        return result["answer"]