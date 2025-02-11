"""Evaluating Copilot for /workspace retrieval"""

import json
import pandas as pd
from typing import List
from pathlib import Path
import numpy as np
from abs_sim_requests import find_retrieved
from base_evaluator import EvaluationResult, Evaluator


def jaccard_similarity(set1, set2):
    """Calculate Jaccard similarity between two sets."""
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union != 0 else 0


def get_overlaps(method, retrieved):
    """Get overlaps between method and retrieved lines."""
    method_lines = {m.strip() for m in method.split("\n")}
    retrieved_lines = [[ri.strip() for ri in set(r.split("\n"))] for r in retrieved]
    scores = [jaccard_similarity(method_lines, rl) for rl in retrieved_lines]
    return scores


def evaluate_test_case(
        self,
        _: Path,
        simulator_output_folder: Path,
        case_number: str,
        test_case_id: str,
        n_id: str,
        __: dict,
        conversation: dict,
        language: str,
        ___: Path,
        outcome: dict,
        ____: List[Path],
    ) -> List[EvaluationResult]:
        """Scores each bug based on whether Copilot answered a workspace query correctly."""

        method = conversation[0]["answer"]
        if "response" not in outcome or outcome["response"] is None:
            score, reason = 0, "No model response found"
            retrieved = ""
            summary = ""
        else:
            summary = outcome["response"].replace("@workspace ", "").strip()
            retrieved = find_retrieved(simulator_output_folder, outcome)
            scores = get_overlaps(method, retrieved)

            # The score is an MRR
            score = 1 / (np.argmax(scores) + 1) if sum(scores) else 0
            reason = "Found overlap between response and expected method" if sum(scores) > 0 else "Did not find overlap between response and expected method"

        results = [
            EvaluationResult(
                self.score_name,
                case_number,
                test_case_id,
                n_id,
                language,
                score,
                reason,
                None,
                None,
                json.dumps({"method": method, "summary": summary, "retrieved": retrieved}),
            )
        ]
        return results

def compute_score_summary(self, evaluation_df: pd.DataFrame) -> List[dict]:
    """Return score summary of workspace evaluation"""
    scores = evaluation_df["score"]
    return [
        {
            "metric": self.score_name,
            "count": len(scores),
            # "Jaccard": round(scores.score.apply(max).mean() * 100, 2),
            "MRR": round(scores.score.mean() * 100, 2),
            # "isfound?": round(scores.isfound.mean() * 100, 2),
        }
    ]
