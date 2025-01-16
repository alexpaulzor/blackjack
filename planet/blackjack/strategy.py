def basic_strategy(
        hand, dealer_upcard_number, can_split=False, can_double_down=False):
    allsplit = {
        2: "split",
        3: "split",
        4: "split",
        5: "split",
        6: "split",
        7: "split",
        8: "split",
        9: "split",
        10: "split",
        1: "split",
    }
    allstand = {
        2: "stand",
        3: "stand",
        4: "stand",
        5: "stand",
        6: "stand",
        7: "stand",
        8: "stand",
        9: "stand",
        10: "stand",
        1: "stand",
    }
    allhit = {
        2: "hit",
        3: "hit",
        4: "hit",
        5: "hit",
        6: "hit",
        7: "hit",
        8: "hit",
        9: "hit",
        10: "hit",
        1: "hit",
    }

    # Pairs
    if can_split:
        # <hand[0].number, <self.dealer.upcard.number, action>>

        plays = {}
        plays[1] = allsplit
        plays[10] = allstand
        plays[9] = {
            2: "split",
            3: "split",
            4: "split",
            5: "split",
            6: "split",
            7: "stand",
            8: "split",
            9: "split",
            10: "stand",
            1: "stand",
        }
        plays[8] = allsplit
        plays[7] = {
            2: "split",
            3: "split",
            4: "split",
            5: "split",
            6: "split",
            7: "split",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[6] = {
            2: "split",
            3: "split",
            4: "split",
            5: "split",
            6: "split",
            7: "hit",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[5] = {
            2: "dbhit",
            3: "dbhit",
            4: "dbhit",
            5: "dbhit",
            6: "dbhit",
            7: "dbhit",
            8: "dbhit",
            9: "dbhit",
            10: "hit",
            1: "hit",
        }
        plays[4] = {
            2: "hit",
            3: "hit",
            4: "hit",
            5: "split",
            6: "split",
            7: "hit",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[3] = {
            2: "split",
            3: "split",
            4: "split",
            5: "split",
            6: "split",
            7: "split",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[2] = plays[3]

        action = plays[hand.cards[0].number][dealer_upcard_number]
        if action == "dbhit":
            if can_double_down:
                return "double_down"
            else:
                return "hit"
        else:
            return action

    # Soft totals
    if hand.has_ace:
        # <hand.soft_sum, <self.dealer.upcard.number, action>>
        plays = {}
        plays[9] = allstand
        plays[8] = allstand
        plays[7] = {
            2: "stand",
            3: "dbstnd",
            4: "dbstnd",
            5: "dbstnd",
            6: "dbstnd",
            7: "stand",
            8: "stand",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[6] = {
            2: "hit",
            3: "dbhit",
            4: "dbhit",
            5: "dbhit",
            6: "dbhit",
            7: "hit",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[5] = {
            2: "hit",
            3: "hit",
            4: "dbhit",
            5: "dbhit",
            6: "dbhit",
            7: "hit",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[4] = plays[5]
        plays[3] = {
            2: "hit",
            3: "hit",
            4: "hit",
            5: "dbhit",
            6: "dbhit",
            7: "hit",
            8: "hit",
            9: "hit",
            10: "hit",
            1: "hit",
        }
        plays[2] = plays[3]

        if hand.soft_sum in plays:
            action = plays[hand.soft_sum][dealer_upcard_number]
            if action == "dbstnd":
                if can_double_down:
                    return "double_down"
                else:
                    return "stand"
            elif action == "dbhit":
                if can_double_down:
                    return "double_down"
                else:
                    return "hit"
            else:
                return action

    # Hard totals
    # <hand.sum, <self.dealer.upcard.number, action>>
    plays = {}
    plays[21] = allstand
    plays[20] = allstand
    plays[19] = allstand
    plays[18] = allstand
    plays[17] = allstand
    plays[16] = {
        2: "stand",
        3: "stand",
        4: "stand",
        5: "stand",
        6: "stand",
        7: "hit",
        8: "hit",
        9: "hit",
        10: "hitstnd",
        1: "hit",
    }
    plays[15] = {
        2: "stand",
        3: "stand",
        4: "stand",
        5: "stand",
        6: "stand",
        7: "hit",
        8: "hit",
        9: "hit",
        10: "hit",
        1: "hit",
    }
    plays[14] = plays[15]
    plays[13] = plays[15]
    plays[12] = {
        2: "hit",
        3: "hit",
        4: "stand",
        5: "stand",
        6: "stand",
        7: "hit",
        8: "hit",
        9: "hit",
        10: "hit",
        1: "hit",
    }
    plays[11] = {
        2: "dbhit",
        3: "dbhit",
        4: "dbhit",
        5: "dbhit",
        6: "dbhit",
        7: "dbhit",
        8: "dbhit",
        9: "dbhit",
        10: "dbhit",
        1: "hit",
    }
    plays[10] = {
        2: "dbhit",
        3: "dbhit",
        4: "dbhit",
        5: "dbhit",
        6: "dbhit",
        7: "dbhit",
        8: "dbhit",
        9: "dbhit",
        10: "hit",
        1: "hit",
    }
    plays[9] = {
        2: "hit",
        3: "dbhit",
        4: "dbhit",
        5: "dbhit",
        6: "dbhit",
        7: "hit",
        8: "hit",
        9: "hit",
        10: "hit",
        1: "hit",
    }
    plays[8] = allhit
    plays[7] = allhit
    plays[6] = allhit
    plays[5] = allhit

    action = plays[hand.sum][dealer_upcard_number]
    if action == "hitstnd":
        if hand.size == 2:
            return "hit"
        else:
            return "stand"
    elif action == "dbhit":
        if can_double_down:
            return "double_down"
        else:
            return "hit"
    else:
        return action
