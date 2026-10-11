# Task 3.3 — Prompt Engineering Portfolio
**Week 3 | Skillset Go EduTech AI/ML Track**

Four prompt-engineering exercises across reasoning, extraction, summarization, and coding. Each one shows
a weak first attempt, what was wrong with it, an improved prompt, and the resulting output.

> **Note:** The outputs below are illustrative drafts written to show the expected effect of each prompt change.
> They were not captured from live runs. **Before submitting, run each prompt yourself in an LLM (Claude, ChatGPT, etc.)
> and replace the outputs with the actual responses**, adjusting the "Problem" and "Takeaway" lines to match what you observe.

---

## 1. Reasoning

**Task:** Get correct, well-justified multi-step arithmetic reasoning out of an LLM.

**Iteration 1 — plain question**
> Prompt: *"A shop had 120 apples. It sold 35% of them in the morning and 40 apples in the afternoon. How many are left?"*
>
> Output: *"The shop has 41 apples left."*

**Problem:** The answer is wrong (no visible work, so the error can't be diagnosed), and the model jumped straight to a number.

**Iteration 2 — add step-by-step instruction + answer tag**
> Prompt: *"A shop had 120 apples. It sold 35% of them in the morning and 40 apples in the afternoon. Work through the problem step by step, showing each calculation, then give the final answer inside <answer></answer> tags."*
>
> Output:
> ```
> Step 1: Apples sold in the morning = 35% of 120 = 0.35 x 120 = 42
> Step 2: Remaining after morning = 120 - 42 = 78
> Step 3: Apples sold in the afternoon = 40
> Step 4: Remaining after afternoon = 78 - 40 = 38
> <answer>38</answer>
> ```

**Result:** Correct (verified by hand: 120 - 42 - 40 = 38) and every step is checkable. The structured tag also makes the final answer trivial to parse programmatically.

**Takeaway:** Asking for step-by-step work doesn't just make reasoning *look* better — it measurably fixes arithmetic errors, because the model commits to intermediate values instead of pattern-matching to a plausible-sounding final number. The output tag is a small addition with a big payoff for any downstream parsing.

---

## 2. Extraction

**Task:** Pull structured fields out of unstructured text reliably.

**Iteration 1 — vague ask**
> Prompt: *"Get the important info from this: 'Please ship 3 units of SKU-4471 to Meera Krishnan at 12 Lake View Road, Chennai 600028 by Friday. Contact: meera.k@example.com, +91-9876543210.'"*
>
> Output: *"The message is about shipping 3 units of SKU-4471 to Meera Krishnan in Chennai by Friday, with her email and phone number provided."*

**Problem:** This is a paraphrase, not extraction — there's no fixed schema, so it can't be fed into a database or spreadsheet without a human rereading it.

**Iteration 2 — explicit schema + strict JSON instruction**
> Prompt: *"Extract the following fields from the text as JSON only, no other text: sku, quantity, recipient_name, address, city, postal_code, deadline, email, phone. Text: 'Please ship 3 units of SKU-4471 to Meera Krishnan at 12 Lake View Road, Chennai 600028 by Friday. Contact: meera.k@example.com, +91-9876543210.'"*
>
> Output:
> ```json
> {
>   "sku": "SKU-4471",
>   "quantity": 3,
>   "recipient_name": "Meera Krishnan",
>   "address": "12 Lake View Road",
>   "city": "Chennai",
>   "postal_code": "600028",
>   "deadline": "Friday",
>   "email": "meera.k@example.com",
>   "phone": "+91-9876543210"
> }
> ```

**Result:** Clean, directly parseable JSON with every requested field correctly separated.

**Takeaway:** Naming the exact fields and demanding a fixed format (JSON, "no other text") turns an open-ended summarization task into something a program can consume directly — the single biggest lever in extraction prompts is specifying the output schema, not describing the task more.

---

## 3. Summarization

**Task:** Get a summary that's both short and keeps the information that actually matters.

**Source text:** *"The Reserve Bank of India kept its benchmark repo rate unchanged at 6.5% for the sixth consecutive meeting, citing persistent food price inflation even as core inflation eased. The central bank also revised its GDP growth forecast for the fiscal year slightly downward, from 7.2% to 6.9%, pointing to weaker-than-expected industrial output and softening export demand. Governor said the committee remains data-dependent and is not ruling out a rate cut later in the year if inflation trends continue to moderate."*

**Iteration 1 — plain "summarize"**
> Prompt: *"Summarize this: [text above]"*
>
> Output: *"The RBI held its repo rate steady at 6.5% due to food inflation, while also lowering its GDP growth forecast slightly because of weaker industrial output. A future rate cut isn't ruled out if inflation eases."*

**Problem:** It's reasonably good, but the length is unpredictable and it's prose, not something easy to scan or drop into a bullet-point report.

**Iteration 2 — fixed length + audience + format constraint**
> Prompt: *"Summarize this for a non-finance audience in exactly 3 bullet points, each under 15 words: [text above]"*
>
> Output:
> ```
> - RBI kept interest rates unchanged at 6.5% again, due to high food prices.
> - GDP growth forecast was lowered slightly, from 7.2% to 6.9%.
> - A rate cut later this year is possible if inflation keeps falling.
> ```

**Result:** Consistently scannable, length-bounded, and jargon-light (e.g. "repo rate" simplified to "interest rate" for the stated non-finance audience).

**Takeaway:** An unconstrained "summarize" prompt gives an unpredictable length and reading level every time. Naming the audience and a hard format constraint (bullet count, word limit) makes the output consistent enough to use in a template or report without manual editing.

---

## 4. Coding

**Task:** Get correct, edge-case-aware code instead of code that only looks right.

**Iteration 1 — minimal ask**
> Prompt: *"Write a Python function to find the second largest number in a list."*
>
> Output:
> ```python
> def second_largest(nums):
>     nums.sort()
>     return nums[-2]
> ```

**Problem:** No handling for duplicate maximums (`[5, 5, 3]` incorrectly returns 5 instead of 3), no handling for a list shorter than 2 elements (crashes), and it mutates the caller's list in place via `.sort()`.

**Iteration 2 — explicit edge cases + constraints**
> Prompt: *"Write a Python function `second_largest(nums)` that returns the second-largest *distinct* value in a list of integers. It must not mutate the input list, must raise a `ValueError` with a clear message if there are fewer than 2 distinct values, and should run in O(n) time, not O(n log n). Include a short docstring and 3 example calls with their expected output as comments."*
>
> Output:
> ```python
> def second_largest(nums):
>     """Return the second-largest distinct value in nums without mutating it.
>     Raises ValueError if nums has fewer than 2 distinct values."""
>     first = second = None
>     for n in nums:
>         if first is None or n > first:
>             first, second = n, first
>         elif n != first and (second is None or n > second):
>             second = n
>     if second is None:
>         raise ValueError("Need at least 2 distinct values")
>     return second
>
> # second_largest([5, 5, 3])      -> 3
> # second_largest([10, 20, 20, 5]) -> 10
> # second_largest([7])             -> raises ValueError
> ```

**Result:** Correct on duplicates, doesn't mutate input, runs in a single O(n) pass, and fails loudly and clearly on invalid input instead of crashing with an unhelpful `IndexError`.

**Takeaway:** A vague coding prompt gets code that handles the "happy path" only. Naming the specific edge cases (duplicates, short lists), a non-functional constraint (don't mutate, time complexity), and asking for usage examples up front catches bugs *before* they're found in review — cheaper than catching them in Task 3.4's audit process.

---

## Overall Findings

| Technique | Effect observed |
|---|---|
| Ask for step-by-step reasoning + an answer tag | Fixed an outright arithmetic error, not just formatting |
| Specify an exact output schema | Turned a paraphrase into directly parseable structured data |
| Add audience + hard length/format constraints | Made summary length and reading level consistent and predictable |
| Name edge cases and non-functional requirements | Caught bugs (duplicates, mutation, missing input validation) before they reached review |

The common thread across all four: **the first version of every prompt was technically a valid request, but
left the output format, scope, and edge cases implicit.** Making those explicit — not writing more words,
but specifying the *right* constraints — was what moved each result from "plausible" to "correct and usable."
