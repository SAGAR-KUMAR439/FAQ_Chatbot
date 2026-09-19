from faqs import faqs, preprocess

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from difflib import SequenceMatcher


# ============================================================
# FAQ CHATBOT
# CodeAlpha - Task 2
# ============================================================


# ============================================================
# 1. COMMON WORDS
# ============================================================

def get_common_words(text1, text2):

    words1 = set(
        preprocess(text1).split()
    )

    words2 = set(
        preprocess(text2).split()
    )

    words1 = words1 - ENGLISH_STOP_WORDS
    words2 = words2 - ENGLISH_STOP_WORDS

    return words1.intersection(words2)


# ============================================================
# 2. TOPIC WORDS
# ============================================================

def get_topic_words(text):

    words = preprocess(text).split()

    generic_words = {
        "python",
        "use",
        "used",
        "tell",
        "explain",
        "work",
        "way",
        "thing",
        "doe",
        "can",
        "could",
        "would",
        "want",
        "need",
        "know",
        "mean",
        "like",
        "please"
    }

    return set(words) - generic_words


# ============================================================
# 3. TOPIC OVERLAP
# ============================================================

def get_topic_overlap(
    user_question,
    faq_question
):

    user_topic_words = get_topic_words(
        user_question
    )

    faq_topic_words = get_topic_words(
        faq_question
    )

    if not faq_topic_words:
        return 0

    common_topic_words = (
        user_topic_words.intersection(
            faq_topic_words
        )
    )

    return (
        len(common_topic_words)
        /
        len(faq_topic_words)
    )


# ============================================================
# 4. CONCEPT / INTENT DETECTION
# ============================================================

def get_concept_words(text):

    text_lower = text.lower()

    processed_words = preprocess(
        text_lower
    ).split()

    concepts = set()


    # ========================================================
    # LOOP COMPARISON
    #
    # Examples:
    # What is the difference between a for loop and a while loop?
    # Difference between for and while
    # for vs while
    # ========================================================

    comparison_phrases = [
        "difference between for and while",
        "difference between a for loop and a while loop",
        "difference between for loop and while loop",
        "for loop vs while loop",
        "for vs while",
        "while vs for",
        "compare for and while",
        "compare a for loop and a while loop",
        "comparison between for and while"
    ]

    for phrase in comparison_phrases:

        if phrase in text_lower:

            concepts.add(
                "loop_comparison"
            )

            break


    # ========================================================
    # WHILE LOOP
    # ========================================================

    if (
        "while loop" in text_lower
        or "while" in processed_words
    ):

        concepts.add(
            "while_loop"
        )


    # ========================================================
    # FOR LOOP
    # ========================================================

    if (
        "for loop" in text_lower
        or (
            "for" in processed_words
            and
            "loop" in processed_words
        )
    ):

        concepts.add(
            "for_loop"
        )


    # ========================================================
    # GENERIC LOOP
    # ========================================================

    if "loop" in processed_words:

        concepts.add(
            "loop"
        )


    # ========================================================
    # LIST ITERATION
    # ========================================================

    list_iteration_phrases = [

        "iterate through a list",
        "iterate through list",

        "iterate over a list",
        "iterate over list",

        "loop through a list",
        "loop through list",

        "loop over a list",
        "loop over list",

        "traverse a list",
        "traverse list",

        "go through a list",
        "go through list",

        "go over a list",
        "go over list"
    ]


    for phrase in list_iteration_phrases:

        if phrase in text_lower:

            concepts.add(
                "list_iteration"
            )

            break


    # ========================================================
    # LIST + ITERATION WORD
    # ========================================================

    iteration_words = {
        "iter",
        "iterate",
        "iteration",
        "iterating",
        "loop",
        "travers",
        "traversing"
    }


    if (
        "list" in processed_words
        and
        any(
            word in processed_words
            for word in iteration_words
        )
    ):

        concepts.add(
            "list_iteration"
        )


    # ========================================================
    # ITERATOR
    # ========================================================

    if (
        "iterator" in text_lower
        or
        "iterators" in text_lower
    ):

        concepts.add(
            "iterator"
        )


    # ========================================================
    # ITERABLE
    # ========================================================

    if (
        "iterable" in text_lower
        or
        "iterables" in text_lower
    ):

        concepts.add(
            "iterable"
        )


    # ========================================================
    # GENERAL ITERATION
    # ========================================================

    if (
        "iteration" in text_lower
        or
        "iterating" in text_lower
        or
        "iterate" in text_lower
        or
        "iter" in processed_words
    ):

        concepts.add(
            "iteration"
        )


    # ========================================================
    # LIST MUTABILITY
    # ========================================================

    if (
        "list" in text_lower
        and
        (
            "change" in text_lower
            or
            "changed" in text_lower
            or
            "modify" in text_lower
            or
            "modified" in text_lower
            or
            "mutable" in text_lower
            or
            "mutability" in text_lower
            or
            "creation" in text_lower
        )
    ):

        concepts.add(
            "list_mutability"
        )


    # ========================================================
    # ERROR HANDLING
    #
    # IMPORTANT:
    # Generic "error" alone is NOT automatically treated
    # as exception handling.
    # ========================================================

    error_handling_phrases = [
        "handle errors",
        "handle error",
        "handling errors",
        "handling error",
        "how to handle errors",
        "how can i handle errors",
        "how do i handle errors",
        "deal with errors",
        "dealing with errors",
        "catch errors",
        "catch an error",
        "catch errors",
        "exception handling",
        "handle exceptions",
        "handling exceptions",
        "try except",
        "try and except",
        "try except block"
    ]


    for phrase in error_handling_phrases:

        if phrase in text_lower:

            concepts.add(
                "exception_handling"
            )

            break


    # Explicit exception words
    if (
        "exception" in text_lower
        or
        "exceptions" in text_lower
    ):

        concepts.add(
            "exception_handling"
        )


    # ========================================================
    # SYNTAX ERROR
    # ========================================================

    if (
        "syntax error" in text_lower
        or
        "syntax errors" in text_lower
    ):

        concepts.add(
            "syntax_error"
        )


    # ========================================================
    # DECORATOR
    # ========================================================

    if (
        "decorator" in text_lower
        or
        "decorators" in text_lower
        or
        "wrapper" in text_lower
        or
        "wrappers" in text_lower
    ):

        concepts.add(
            "decorator"
        )


    # ========================================================
    # INHERITANCE
    # ========================================================

    if (
        "inheritance" in text_lower
        or
        "inherit" in text_lower
        or
        "inherited" in text_lower
        or
        "parent class" in text_lower
        or
        "child class" in text_lower
    ):

        concepts.add(
            "inheritance"
        )


    # ========================================================
    # FUNCTION
    # ========================================================

    if (
        "function" in text_lower
        or
        "functions" in text_lower
    ):

        concepts.add(
            "function"
        )


    # ========================================================
    # VARIABLE
    # ========================================================

    if (
        "variable" in text_lower
        or
        "variables" in text_lower
    ):

        concepts.add(
            "variable"
        )


    # ========================================================
    # STRING
    # ========================================================

    if (
        "string" in text_lower
        or
        "strings" in text_lower
    ):

        concepts.add(
            "string"
        )


    # ========================================================
    # TUPLE
    # ========================================================

    if (
        "tuple" in text_lower
        or
        "tuples" in text_lower
    ):

        concepts.add(
            "tuple"
        )


    # ========================================================
    # DICTIONARY
    # ========================================================

    if (
        "dictionary" in text_lower
        or
        "dictionaries" in text_lower
        or
        "dict" in text_lower
    ):

        concepts.add(
            "dictionary"
        )


    # ========================================================
    # SET
    # ========================================================

    if (
        "set" in text_lower
        or
        "sets" in text_lower
    ):

        concepts.add(
            "set"
        )


    # ========================================================
    # OOP
    # ========================================================

    if (
        "class" in text_lower
        or
        "object" in text_lower
        or
        "oop" in text_lower
        or
        "object oriented" in text_lower
    ):

        concepts.add(
            "oop"
        )


    return concepts


# ============================================================
# 5. CONCEPT SCORE
# ============================================================

def get_concept_score(
    user_question,
    faq_question
):

    user_concepts = get_concept_words(
        user_question
    )

    faq_concepts = get_concept_words(
        faq_question
    )


    if not user_concepts:
        return 0


    # ========================================================
    # LOOP COMPARISON
    # ========================================================

    if "loop_comparison" in user_concepts:

        if "loop_comparison" in faq_concepts:
            return 1.0

        # A FAQ containing both for + while but not explicitly
        # comparison gets only a weak score.
        if (
            "for_loop" in faq_concepts
            and
            "while_loop" in faq_concepts
        ):
            return 0.30


    # ========================================================
    # LIST ITERATION
    # ========================================================

    if "list_iteration" in user_concepts:

        if "list_iteration" in faq_concepts:
            return 1.0

        if "for_loop" in faq_concepts:
            return 0.90

        if "iteration" in faq_concepts:
            return 0.45

        if "iterator" in faq_concepts:
            return 0.20

        if "iterable" in faq_concepts:
            return 0.15

        if "loop" in faq_concepts:
            return 0.35


    # ========================================================
    # ITERATOR
    # ========================================================

    if "iterator" in user_concepts:

        if "iterator" in faq_concepts:
            return 1.0

        if "iterable" in faq_concepts:
            return 0.40

        if "iteration" in faq_concepts:
            return 0.35

        if "for_loop" in faq_concepts:
            return 0.20


    # ========================================================
    # ITERABLE
    # ========================================================

    if "iterable" in user_concepts:

        if "iterable" in faq_concepts:
            return 1.0

        if "iterator" in faq_concepts:
            return 0.40

        if "iteration" in faq_concepts:
            return 0.30

        if "for_loop" in faq_concepts:
            return 0.20


    # ========================================================
    # GENERAL ITERATION
    # ========================================================

    if "iteration" in user_concepts:

        if "list_iteration" in faq_concepts:
            return 0.85

        if "for_loop" in faq_concepts:
            return 0.60

        if "iterator" in faq_concepts:
            return 0.50

        if "iterable" in faq_concepts:
            return 0.40

        if "iteration" in faq_concepts:
            return 1.0


    # ========================================================
    # WHILE LOOP
    # ========================================================

    if "while_loop" in user_concepts:

        if "while_loop" in faq_concepts:
            return 1.0

        if "for_loop" in faq_concepts:
            return 0.0

        if "loop" in faq_concepts:
            return 0.30


    # ========================================================
    # FOR LOOP
    # ========================================================

    if "for_loop" in user_concepts:

        if "for_loop" in faq_concepts:
            return 1.0

        if "while_loop" in faq_concepts:
            return 0.0

        if "loop" in faq_concepts:
            return 0.30


    # ========================================================
    # LIST MUTABILITY
    # ========================================================

    if "list_mutability" in user_concepts:

        if "list_mutability" in faq_concepts:
            return 1.0


    # ========================================================
    # EXCEPTION HANDLING
    # ========================================================

    if "exception_handling" in user_concepts:

        if "exception_handling" in faq_concepts:
            return 1.0

        if "syntax_error" in faq_concepts:
            return 0.0


    # ========================================================
    # SYNTAX ERROR
    # ========================================================

    if "syntax_error" in user_concepts:

        if "syntax_error" in faq_concepts:
            return 1.0

        if "exception_handling" in faq_concepts:
            return 0.0


    # ========================================================
    # DECORATOR
    # ========================================================

    if "decorator" in user_concepts:

        if "decorator" in faq_concepts:
            return 1.0


    # ========================================================
    # INHERITANCE
    # ========================================================

    if "inheritance" in user_concepts:

        if "inheritance" in faq_concepts:
            return 1.0


    # ========================================================
    # GENERIC SPECIFIC CONCEPT MATCH
    # ========================================================

    specific_concepts = {
        "loop_comparison",
        "while_loop",
        "for_loop",
        "list_iteration",
        "list_mutability",
        "iterator",
        "iterable",
        "exception_handling",
        "syntax_error",
        "decorator",
        "inheritance"
    }


    user_specific = (
        user_concepts.intersection(
            specific_concepts
        )
    )

    faq_specific = (
        faq_concepts.intersection(
            specific_concepts
        )
    )


    if (
        not user_specific
        or
        not faq_specific
    ):

        return 0


    common_concepts = (
        user_specific.intersection(
            faq_specific
        )
    )


    return (
        len(common_concepts)
        /
        len(user_specific)
    )


# ============================================================
# 6. PREPARE FAQ QUESTIONS
# ============================================================

questions = [
    faq["processed_question"]
    for faq in faqs
]


# ============================================================
# 7. TF-IDF
# ============================================================

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    questions
)


# ============================================================
# 8. CHATBOT LOOP
# ============================================================

while True:

    user_question = input(
        "\nYou: "
    )


    # ========================================================
    # EMPTY INPUT
    # ========================================================

    if not user_question.strip():

        print(
            "\nChatbot: Please enter a question."
        )

        continue


    # ========================================================
    # EXIT
    # ========================================================

    if user_question.lower().strip() in {
        "exit",
        "quit"
    }:

        print(
            "\nChatbot: Goodbye!"
        )

        break


    # ========================================================
    # EXACT MATCH
    # ========================================================

    normalized_user_question = (
        user_question
        .strip()
        .lower()
    )


    exact_match_index = -1


    for index, faq in enumerate(faqs):

        normalized_faq_question = (
            faq["question"]
            .strip()
            .lower()
        )


        if (
            normalized_user_question
            ==
            normalized_faq_question
        ):

            exact_match_index = index

            break


    # ========================================================
    # EXACT MATCH RESPONSE
    # ========================================================

    if exact_match_index != -1:

        print(
            "\nMatched FAQ:",
            faqs[
                exact_match_index
            ]["question"]
        )


        print(
            "\nChatbot Answer:"
        )


        print(
            faqs[
                exact_match_index
            ]["answer"]
        )


        continue


    # ========================================================
    # PREPROCESS
    # ========================================================

    processed_user_question = preprocess(
        user_question
    )


    print(
        "Processed:",
        processed_user_question
    )


    # ========================================================
    # USER VECTOR
    # ========================================================

    user_vector = vectorizer.transform(
        [processed_user_question]
    )


    # ========================================================
    # TF-IDF SIMILARITIES
    # ========================================================

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )[0]


    # ========================================================
    # USER CONCEPTS
    # ========================================================

    user_concepts = get_concept_words(
        user_question
    )


    # ========================================================
    # BEST MATCH
    # ========================================================

    best_match_index = -1

    best_combined_similarity = -1

    best_scores = {}


    # ========================================================
    # SCORE ALL FAQs
    # ========================================================

    for index, faq in enumerate(faqs):


        # ----------------------------------------------------
        # TF-IDF
        # ----------------------------------------------------

        tfidf_score = similarities[index]


        # ----------------------------------------------------
        # TEXT SIMILARITY
        # ----------------------------------------------------

        text_similarity = SequenceMatcher(
            None,
            user_question.lower(),
            faq["question"].lower()
        ).ratio()


        # ----------------------------------------------------
        # COMMON WORDS
        # ----------------------------------------------------

        common_words = get_common_words(
            user_question,
            faq["question"]
        )


        # ----------------------------------------------------
        # FAQ WORDS
        # ----------------------------------------------------

        faq_processed_words = set(
            preprocess(
                faq["question"]
            ).split()
        )


        # ----------------------------------------------------
        # COMMON WORD SCORE
        # ----------------------------------------------------

        common_word_score = (
            len(common_words)
            /
            max(
                len(faq_processed_words),
                1
            )
        )


        # ----------------------------------------------------
        # TOPIC OVERLAP
        # ----------------------------------------------------

        topic_overlap = get_topic_overlap(
            user_question,
            faq["question"]
        )


        # ----------------------------------------------------
        # FAQ CONCEPTS
        # ----------------------------------------------------

        faq_concepts = get_concept_words(
            faq["question"]
        )


        # ----------------------------------------------------
        # CONCEPT SCORE
        # ----------------------------------------------------

        concept_score = get_concept_score(
            user_question,
            faq["question"]
        )


        # ====================================================
        # BASE SCORE
        # ====================================================

        combined_similarity = (

            0.30 * tfidf_score

            +
            0.15 * text_similarity

            +
            0.10 * common_word_score

            +
            0.20 * topic_overlap

            +
            0.25 * concept_score
        )


        # ====================================================
        # CONCEPT BONUS / PENALTY
        # ====================================================

        concept_bonus = 0


        # ----------------------------------------------------
        # LOOP COMPARISON
        # ----------------------------------------------------

        if (
            "loop_comparison"
            in user_concepts
        ):

            if (
                "loop_comparison"
                in faq_concepts
            ):

                concept_bonus += 0.50


            elif (
                "for_loop"
                in faq_concepts
                and
                "while_loop"
                in faq_concepts
            ):

                concept_bonus -= 0.20


            else:

                concept_bonus -= 0.10


        # ----------------------------------------------------
        # LIST ITERATION
        # ----------------------------------------------------

        if (
            "list_iteration"
            in user_concepts
        ):

            if (
                "list_iteration"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "for_loop"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "iterator"
                in faq_concepts
            ):

                concept_bonus -= 0.10


            elif (
                "iterable"
                in faq_concepts
            ):

                concept_bonus -= 0.15


            elif (
                "loop"
                in faq_concepts
            ):

                concept_bonus += 0.05


        # ----------------------------------------------------
        # ITERATOR
        # ----------------------------------------------------

        if (
            "iterator"
            in user_concepts
        ):

            if (
                "iterator"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "iterable"
                in faq_concepts
            ):

                concept_bonus -= 0.05


        # ----------------------------------------------------
        # ITERABLE
        # ----------------------------------------------------

        if (
            "iterable"
            in user_concepts
        ):

            if (
                "iterable"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "iterator"
                in faq_concepts
            ):

                concept_bonus -= 0.05


        # ----------------------------------------------------
        # WHILE LOOP
        # ----------------------------------------------------

        if (
            "while_loop"
            in user_concepts
            and
            "loop_comparison"
            not in user_concepts
        ):

            if (
                "while_loop"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "for_loop"
                in faq_concepts
            ):

                concept_bonus -= 0.20


        # ----------------------------------------------------
        # FOR LOOP
        # ----------------------------------------------------

        if (
            "for_loop"
            in user_concepts
            and
            "loop_comparison"
            not in user_concepts
        ):

            if (
                "for_loop"
                in faq_concepts
            ):

                concept_bonus += 0.20


            elif (
                "while_loop"
                in faq_concepts
            ):

                concept_bonus -= 0.20


        # ----------------------------------------------------
        # LIST MUTABILITY
        # ----------------------------------------------------

        if (
            "list_mutability"
            in user_concepts
            and
            "list_mutability"
            in faq_concepts
        ):

            concept_bonus += 0.20


        # ----------------------------------------------------
        # EXCEPTION HANDLING
        # ----------------------------------------------------

        if (
            "exception_handling"
            in user_concepts
        ):

            if (
                "exception_handling"
                in faq_concepts
            ):

                concept_bonus += 0.25


            elif (
                "syntax_error"
                in faq_concepts
            ):

                concept_bonus -= 0.20


        # ----------------------------------------------------
        # SYNTAX ERROR
        # ----------------------------------------------------

        if (
            "syntax_error"
            in user_concepts
        ):

            if (
                "syntax_error"
                in faq_concepts
            ):

                concept_bonus += 0.25


            elif (
                "exception_handling"
                in faq_concepts
            ):

                concept_bonus -= 0.20


        # ----------------------------------------------------
        # DECORATOR
        # ----------------------------------------------------

        if (
            "decorator"
            in user_concepts
            and
            "decorator"
            in faq_concepts
        ):

            concept_bonus += 0.20


        # ----------------------------------------------------
        # INHERITANCE
        # ----------------------------------------------------

        if (
            "inheritance"
            in user_concepts
            and
            "inheritance"
            in faq_concepts
        ):

            concept_bonus += 0.20


        # ====================================================
        # FINAL SCORE
        # ====================================================

        combined_similarity += (
            concept_bonus
        )


        # ====================================================
        # CLAMP SCORE
        # ====================================================

        combined_similarity = max(
            0,
            min(
                combined_similarity,
                1
            )
        )


        # ====================================================
        # BEST MATCH
        # ====================================================

        if (
            combined_similarity
            >
            best_combined_similarity
        ):

            best_combined_similarity = (
                combined_similarity
            )

            best_match_index = index

            best_scores = {

                "tfidf":
                    tfidf_score,

                "text_similarity":
                    text_similarity,

                "common_words":
                    common_words,

                "common_word_score":
                    common_word_score,

                "topic_overlap":
                    topic_overlap,

                "concept_score":
                    concept_score,

                "concept_bonus":
                    concept_bonus
            }


    # ========================================================
    # DISPLAY MATCHED FAQ
    # ========================================================

    print(
        "\nMatched FAQ:",
        faqs[
            best_match_index
        ]["question"]
    )


    # ========================================================
    # DEBUG SCORES
    # ========================================================

    print(
        "TF-IDF similarity:",
        best_scores["tfidf"]
    )

    print(
        "Common words:",
        best_scores["common_words"]
    )

    print(
        "Common word count:",
        len(
            best_scores["common_words"]
        )
    )

    print(
        "Text similarity:",
        best_scores["text_similarity"]
    )

    print(
        "Common word score:",
        best_scores["common_word_score"]
    )

    print(
        "Topic overlap:",
        best_scores["topic_overlap"]
    )

    print(
        "Concept score:",
        best_scores["concept_score"]
    )

    print(
        "Concept bonus:",
        best_scores["concept_bonus"]
    )

    print(
        "Combined similarity:",
        best_combined_similarity
    )


    # ========================================================
    # ACCEPTANCE LOGIC
    # ========================================================

    tfidf_score = best_scores[
        "tfidf"
    ]

    text_score = best_scores[
        "text_similarity"
    ]

    concept_score = best_scores[
        "concept_score"
    ]

    topic_score = best_scores[
        "topic_overlap"
    ]


    # --------------------------------------------------------
    # STRONG NORMAL MATCH
    # --------------------------------------------------------

    strong_match = (
        best_combined_similarity
        >=
        0.68
    )


    # --------------------------------------------------------
    # VERY STRONG TEXT MATCH
    # --------------------------------------------------------

    very_strong_match = (

        tfidf_score >= 0.85

        and

        text_score >= 0.75
    )


    # --------------------------------------------------------
    # STRONG CONCEPT MATCH
    # --------------------------------------------------------

    strong_concept_match = (

        concept_score == 1.0

        and

        (
            tfidf_score >= 0.30

            or

            topic_score >= 0.30
        )
    )


    # ========================================================
    # SPECIAL INTENT ACCEPTANCE
    # ========================================================

    special_intent_match = False


    # --------------------------------------------------------
    # LOOP COMPARISON
    # --------------------------------------------------------

    if (
        "loop_comparison"
        in user_concepts
        and
        "loop_comparison"
        in get_concept_words(
            faqs[
                best_match_index
            ]["question"]
        )
    ):

        special_intent_match = True


    # --------------------------------------------------------
    # LIST ITERATION
    # --------------------------------------------------------

    if (
        "list_iteration"
        in user_concepts
        and
        (
            "for_loop"
            in get_concept_words(
                faqs[
                    best_match_index
                ]["question"]
            )

            or

            "list_iteration"
            in get_concept_words(
                faqs[
                    best_match_index
                ]["question"]
            )
        )
    ):

        special_intent_match = True


    # --------------------------------------------------------
    # EXCEPTION HANDLING
    # --------------------------------------------------------

    if (
        "exception_handling"
        in user_concepts
        and
        "exception_handling"
        in get_concept_words(
            faqs[
                best_match_index
            ]["question"]
        )
    ):

        special_intent_match = True


    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    if (
        strong_match
        or
        very_strong_match
        or
        strong_concept_match
        or
        special_intent_match
    ):

        best_answer = faqs[
            best_match_index
        ]["answer"]


        print(
            "\nChatbot Answer:"
        )


        print(
            best_answer
        )


    else:

        print(
            "\nChatbot Answer:"
        )


        print(
            "Sorry, I don't know the answer to that question."
        )
