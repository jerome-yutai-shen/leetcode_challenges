# -*- coding: utf-8 -*-
"""
Created on Jun 05 06:31:16 2022

@author: Jerome Yutai Shen

"""
from typing import Tuple, Dict
from enum import Enum, unique


@unique
class Door(Enum):
    A = 1
    B = 2


@unique
class Correctness(Enum):
    True_Positive = (True, True) # "b11"
    True_Negative = (False, False)
    False_Positive = (False, True)
    False_Negative = (True, False) # "b10"


correctness_alias = {_k: _k.name.replace("_", " ") for _k in Correctness}


def liar_reply(groud_truth: bool, predict: bool) -> bool:
    return groud_truth != predict


def truth_teller_reply(groud_truth: bool, predict: bool) -> bool:
    return groud_truth == predict


def question_either_guard(predict_treature: bool,
                          predict_guard_my_predict_treasure: bool,
                          door_id: Enum = Door.A,
                          if_print: bool = True) -> Dict:
    """
    f((bool: predict treasure is here, bool: predict the guard will affirm me)) -> bool: in fact, treasure is here or NOT
    :param predict_treature:
    :param predict_guard_my_predict_treasure:
    :param if_print:
    :return:
    """
    grouth_truth_vs_inferred_treasure_existence = {True: None, False: None}
    all_doors = (Door.B, Door.A)
    if door_id == Door.B:
        all_doors = all_doors[::-1]

    for groud_truth in grouth_truth_vs_inferred_treasure_existence:

        true_guard_tt_reply = truth_teller_reply(groud_truth, predict_treature)
        test_tt = truth_teller_reply(true_guard_tt_reply, predict_guard_my_predict_treasure)

        true_guard_l_reply = liar_reply(groud_truth, predict_treature)
        test_l = liar_reply(true_guard_l_reply, predict_guard_my_predict_treasure)

        assert test_tt == test_l

        test_result = (test_tt and test_l) if predict_guard_my_predict_treasure else not (test_tt and test_l)
        inferred_treasure_existence = predict_treature if test_result else not predict_treature

        assert groud_truth == inferred_treasure_existence

        grouth_truth_vs_inferred_treasure_existence[groud_truth] = inferred_treasure_existence

        if if_print:
            print(f"#####")
            print(f"The ground truth: {groud_truth}")
            print(f"You guess treasure exists in {door_id}: {predict_treature}")
            print(f"You guess either guard tells your guess is correct or wrong: {predict_guard_my_predict_treasure}")
            print(f"Either guard affirms or denies your guess: {(test_tt and test_l)}")
            print(f"your inference: {inferred_treasure_existence}")
            print(f"You should go to door {all_doors[inferred_treasure_existence]}")
            print(f"Correctness: {correctness_alias.get(Correctness((groud_truth, predict_treature)))}")
    # if if_print:
    #     print(f"When the treasure is behind the door, and your inference: {grouth_truth_vs_inferred_treasure_existence.get(True)}")
    #     print(f"When the treasure is NOT behind the door, and your inference: {grouth_truth_vs_inferred_treasure_existence.get(False)}")

    return grouth_truth_vs_inferred_treasure_existence


def test_case(door_id: Enum = Door.A):
    for ground_tructh_predict in Correctness: 
        print(f"________\n")
        predict_treature, predict_guard = ground_tructh_predict.value
        question_either_guard(bool(predict_treature), bool(predict_guard), door_id)


if __name__ == "__main__":
    test_case(Door.B)
