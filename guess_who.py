if has_facial_hair or is_black:
    if is_black or has_brown_hair:
        if has_beard or wears_glasses:
            one_by_one('Andy','James','Sarah')
        else:
            one_by_one('Daniel','Connor','Justin')
    else:
        if has_beard:
            one_by_one('David','Jon','William')
        else:
            one_by_one('Jake','Joshua','Tyler')
else:
    if is_bald or is_blonde:
        if has_blue_eyes:
            one_by_one('Kyle','Megan','Nick')
        else:
            one_by_one('Alex','Brandon','Zachary')
    else:
        if wears_hat:
            one_by_one('Ashley','Chris','Rachael')
        else:
            one_by_one('Emily','Joseph','Matt')
def one_by_one(person1,person2,person3):
    '''You'll just have to check each one individually at this point.'''