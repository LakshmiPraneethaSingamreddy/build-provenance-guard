# Acceptance criteria — Provenance Guard
---
## 1. Out of 5 pieces I wrote myself atmost only 1 of them should receive highly-AI label.

**Why this target:**
Because human writing can sometimes be simple and predictable, the system may mistake it for AI-generated text. Limiting high-confidence AI labels to no more than 1 out of 5 human-written samples helps reduce unfair accusations.

---

## 2. For 3 of 3 invalid cases, which have missing text, empty text or text: null, the service should return a clear error response instead of attempting classification and each response should explain there is no text to analyze.


**Why this target:**
A missing, empty, or null text value cannot be analyzed. The service should clearly explain that there is no text to classify instead of attempting to generate misleading scores or labels.


---

## 3. Across five test cases, the system should produce all three labels—human, ai, and unsure—at least once.

**Why this target:**
All three labels—human, unsure, and ai—must be reachable across the test submissions. This confirms that the score thresholds work correctly and that the system can represent different levels of confidence

---

## 4. For all 5 of 5 valid appeal cases, every appeal should return a successful response, change the submission status to under_review and create an appeal entry in the audit log.

**Why this target:**
Users should have a way to challenge an incorrect classification. Every valid appeal should change the submission status to under_review and create an audit-log entry so the appeal can be tracked.


---

## 5. For atlest 4 of 5 cases, the absolute difference between model_score and style_score should be less than 0.30.

**Why this target:**
The model and style scores look at different parts of the same text, so they may not always match exactly. Getting their difference below `0.30` in at least 4 out of 5 cases shows that they usually give reasonable results. If the scores differ a lot, it might indicate that one signal might be affected by its blind spot.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
