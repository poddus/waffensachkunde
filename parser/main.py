import re
from dataclasses import dataclass
import csv
import logging
import numpy as np
import pandas as pd


@dataclass()
class MultipleChoice:
    """
    blah
    """
    q_id: str
    question: str
    choices: list
    answer: list

    pass


@dataclass()
class MCQuestionInput:
    q_id: str
    question: str

    pass


@dataclass()
class MCAnswerInput:
    q_id: str
    choices: list
    answer: list

    pass


def separate_question_records(q_txt) -> list[list]:
    pass


def separate_answer_records(a_txt):
    """return list of records (list of list of strings)"""

    records = []
    current_record = []
    for line in a_txt:
        if re.match('\n', line):
            logging.debug('delimiter encountered')
            records.append(current_record)
            current_record = []
            continue
        current_record.append(line.rstrip())
    # add last record to list
    records.append(current_record)

    list_of_mcai = []
    for rec in records:
        current_mcai = MCAnswerInput
        pass

    answers = list_of_mcai


def combine_q_and_a(questions: MCQuestionInput, answers: MCAnswerInput) -> MultipleChoice:
    pass


def main():
    with open('../preparsed/answers_only_multiple_choice.txt', 'r') as f:
        a_txt = f.readlines()
    answer_records = separate_answer_records(a_txt)
    pass


main()
