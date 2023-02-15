from os import system, name

yes = True
no = False
bmpd_lt_1 = '< 1 per day'
bmpd_nc = 'Not constant'
bmpd_lt_5 = '> 2 and <= 5 per day'
bmpd_gt_5_and_lt_10 = ' > 5 and < 10 per day'
bmpd_gt_10 = '>= 10 per day'
bmpd_dict = {
    1: bmpd_lt_5,
    2: bmpd_gt_5_and_lt_10,
    3: bmpd_gt_10,
    4: bmpd_nc,
    5: bmpd_lt_1
}
blood_with_stool = 'blood_with_stool'
bis_continuous = 'Continuous'
bis_frequent = 'Most of the time'
bis_rare = 'Rarely'
bis_no = 'None'
bis_dict = {
    1: bis_continuous,
    2: bis_frequent,
    3: bis_rare,
}
bis_dict1 = {
    1: bis_continuous,
    2: bis_frequent,
    3: bis_rare,
    4: bis_no
}
diarrhea = 'diarrhea'
constipation = 'constipation'
alternate = 'both alternate'
stool_dict = {
    1: diarrhea,
    2: constipation,
    3: alternate,
    4: None
}

stool_dict1 = {
    1: diarrhea,
    2: constipation,
    3: alternate,
}

ibs = 'ibs'
ibd = 'ibd'
uc = 'uc'
crohn = 'crohn'
mild_uc = 'mild_uc'
severe_uc = 'severe_uc'
fulminant_uc = 'fulminant_uc'
mild_crohn = 'mild_crohn'
severe_crohn = 'severe_crohn'
anemia = 'anemia'

fistula = 'fistula'
mouth_sores = 'mouth_sores'
uc_type = 'uc_type'
crohn_type = ''
tachycardia = 'tachycardia'
bloating = 'bloating'
tenesmus = 'tenesmus'
mucus_with_stool = 'mucus_with_stool'
abdominal_pain = 'abdominal_pain'
stool_type = 'stool_type'
eye_redness = 'eye_redness'
eye_pain = 'eye_pain'
joint_pain = 'joint_pain'
joint_soreness = 'joint_soreness'
red_tender_bumps_under_the_skin = 'red_tender_bumps_under_the_skin'
fatigue = 'fatigue'
which = 'which'
pus_with_stool = 'pus_with_stool'
abdomen_cramps = 'abdomen_cramps'
bowel_movements_per_day = 'bowel_movements_per_day'
disease = ''
blood_with_stool_frequency = 'blood_with_stool_frequency'
tiredness = 'tiredness'
fever = 'fever'
nausea = 'nausea'
vomiting = 'vomiting'
weight_loss = 'weight_loss'
appetite_loss = 'appetite_loss'
tested_for_anemia = 'tested_for_anemia'
weakness = 'weakness'
pale_skin = 'pale_skin'
yellowish_skin = 'yellowish_skin'
irregular_heart_beat = 'irregular_heart_beat'
shortness_of_breath = 'shortness_of_breath'
dizziness = 'dizziness'
lightheadedness = 'lightheadedness'
chest_pain = 'chest_pain'
cold_hands = 'cold_hands'
cold_feet = 'cold_feet'
headache = 'headache'
brittle_nails = 'brittle_nails'
diagnosis = 'diagnosis'

unknown = 'unknown'


def get_answer(to_ask: str, tuple_facts: dict = None):
    if tuple_facts is None:
        answer = input('\n' + to_ask)
        if answer.lower() in ['y', 'yes']:
            return yes
        elif answer.lower() in ['n', 'no']:
            return no
        else:
            print(f'{answer} is not valid.')
            return get_answer(to_ask)
    else:
        answer = (input('\n' + to_ask + f'[reply with a number between 1 and {len(tuple_facts)}]\n'))
        if answer.isnumeric():
            if int(answer) in range(1, len(tuple_facts) + 1):
                return tuple_facts[int(answer)]
            else:
                print(f'{answer} is not valid.')
                get_answer(to_ask, tuple_facts)
        else:
            print(f'{answer} is not valid.')
            get_answer(to_ask, tuple_facts)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# ******************************************************************************************************************
#
# ******************************************************************************************************************
