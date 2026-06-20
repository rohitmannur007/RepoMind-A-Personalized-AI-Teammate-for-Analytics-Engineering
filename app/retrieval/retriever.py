from __future__ import annotations

from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RepoRetriever:
    def __init__(self, documents: list[dict[str, Any]]):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = None

        texts = [doc["content"] for doc in documents]
        if texts:
            self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        if not self.documents or self.matrix is None:
            return []

        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix)[0]
        ranked = scores.argsort()[::-1][:top_k]

        results = []
        for idx in ranked:
            doc = self.documents[idx]
            content = doc["content"].replace("\n", " ")
            snippet = content[:400] + ("..." if len(content) > 400 else "")
            results.append(
                {
                    "path": doc["path"],
                    "score": float(scores[idx]),
                    "snippet": snippet,
                }
            )
        return results