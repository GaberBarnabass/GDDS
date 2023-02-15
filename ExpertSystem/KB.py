from ExpertSystem.CustomFacts import *
from utility_package.utils import *


class ES(KnowledgeEngine):
    """def declared(self, symptom: str):
        for index in range(1, len(self.facts)):
            for key in self.facts[index]:
                if key == symptom:
                    return True
        return False"""

    # ******************************************************************************************************************
    # irritable bowel syndrome
    # ******************************************************************************************************************

    @Rule(salience=1000)
    def bloating(self):
        self.declare(Symptom(bloating=get_answer('Are you feeling bloated? ')))

    @Rule(salience=1000)
    def tenesmus(self):
        self.declare(Symptom(tenesmus=get_answer('Do you suffer from tenesmus? ')))

    @Rule(salience=1000)
    def mucus_with_stool(self):
        self.declare(Symptom(mucus_with_stool=get_answer('Do you observe mucus with your stool? ')))

    @Rule(salience=1000)
    def abdominal_pain(self):
        self.declare(Symptom(abdominal_pain=get_answer('Do you experience abdominal pain? ')))

    @Rule(salience=1000)
    def abdominal_cramps(self):
        self.declare(Symptom(abdomen_cramps=get_answer('Do you experience abdominal cramps? ')))

    @Rule(salience=1000)
    def stool_type(self):
        ans = get_answer('Do you suffer from\n'
                         '1)diarrhea,\n'
                         '2)constipation,\n'
                         '3)both alternate,\n'
                         '4)None of these\n', stool_dict)
        self.declare(Symptom(stool_type=ans))

    @Rule(salience=1000)
    def pus_with_stool(self):
        self.declare(Symptom(pus_with_stool=get_answer('Do you observe pus in your stool? ')))

    @Rule(salience=1000)
    def blood_with_stool(self):
        self.declare(Symptom(blood_with_stool=get_answer('Do you observe blood with your stool? ')))

    @Rule(Symptom(blood_with_stool=yes), salience=1000)
    def blood_with_stool_frequency(self):
        ans = get_answer('\nHow often do you observe blood with stool?\n'
                         '1) Continuously,\n'
                         '2) Most of the time,\n'
                         '3) Rarely\n', bis_dict)
        self.declare(Symptom(blood_with_stool_frequency=ans))

    # ******************************************************************************************************************
    # checking for ibs
    # ******************************************************************************************************************

    @Rule(
        AND(
            Symptom(bloating=yes),
            Symptom(tenesmus=yes),
            Symptom(mucus_with_stool=yes),
            Symptom(pus_with_stool=no),
            Symptom(abdominal_pain=yes),
            Symptom(abdomen_cramps=no),
            NOT(Symptom(stool_type=None)),
            OR(
                AND(
                    OR(
                        Symptom(blood_with_stool=no),
                        AND(
                            Symptom(blood_with_stool=yes),
                            Symptom(blood_with_stool_frequency=bis_rare))
                    ),
                    Symptom(stool_type=L(constipation) | L(alternate))
                ),
                AND(
                    Symptom(blood_with_stool=no),
                    Symptom(stool_type=diarrhea)
                )

            )
        ),
        salience=2000)
    def is_ibs(self):
        # ibs <- bloating & tenesmus & mucus_with_stool & abdominal_pain & (diarrhea | constipation | both_alternate).

        self.declare(Disease(ibs=yes))

    # ******************************************************************************************************************
    # checking for ibd
    # ******************************************************************************************************************
    @Rule(
        AND(
            NOT(Disease(ibs=yes)),
            Symptom(stool_type=diarrhea),
            Symptom(abdominal_pain=yes),
            Symptom(abdomen_cramps=yes),
            OR(
                Symptom(bloating=yes),
                Symptom(bloating=no)
            )
        ),
        salience=1999)
    def is_ibd(self):
        # print('entering ibd')
        self.declare(Disease(ibd=yes))

    # ******************************************************************************************************************
    # checking for ulcerative colitis
    # ******************************************************************************************************************

    @Rule(
        AND(
            Disease(ibd=yes),
            OR(
                Symptom(mucus_with_stool=yes),
                Symptom(pus_with_stool=yes),
            ),
            Symptom(tenesmus=yes)
        ),
        salience=1998
    )
    def ulcerative_colitis(self):
        self.declare(Disease(uc=yes))

    # ******************************************************************************************************************
    # if uc define the severity
    # ******************************************************************************************************************

    # ******************************************************************************************************************
    # mild ulcerative colitis
    # ******************************************************************************************************************

    @Rule(Disease(ibd=yes), salience=965)
    def bowel_movements_per_day(self):
        ans = get_answer('How often do you need to have a bowel movement?\n'
                         '1) > 2 and <= 5 per day,\n'
                         '2) > 5 and < 10 per day,\n'
                         '3) >= 10 per day\n', bmpd_dict)
        self.declare(Symptom(bowel_movements_per_day=ans))

    @Rule(
        AND(
            Disease(uc=yes),
            Symptom(bowel_movements_per_day=bmpd_lt_5),
            OR(
                Symptom(blood_with_stool=no),
                Symptom(blood_with_stool_frequency=bis_rare)
            )
        ),
        salience=1997
    )
    def mild_ulcerative_colitis(self):
        # print('mild uc detected.')
        self.declare(Disease(mild_uc=yes))

    # ******************************************************************************************************************
    # anemia, frequent in crohn's disease and severe and fulminant ulcerative colitis due to bleeding
    # ******************************************************************************************************************

    @Rule(Disease(ibd=yes), salience=950)
    def tested_for_anemia(self):
        self.declare(Fact(tested_for_anemia=get_answer('Did you have been tested for anemia?\n')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=yes)), salience=945)
    def anemia_result(self):
        ans = get_answer('Did you result positive to anemia? ')
        if ans == yes:
            self.declare(Symptom(anemia=yes))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=945)
    def irregular_heart_beat(self):
        self.declare(Symptom(irregular_heart_beat=get_answer('Do you have an irregular heart beat? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no), Symptom(irregular_heart_beat=yes)), salience=945)
    def tachycardia(self):
        self.declare(Symptom(tachycardia=get_answer('Do you suffer from tachycardia? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def pale_skin(self):
        self.declare(Symptom(pale_skin=get_answer('Do you experience pale skin? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def fatigue(self):
        self.declare(Symptom(fatigue=get_answer('Do you experience a feel of fatigue? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def weakness(self):
        self.declare(Symptom(weakness=get_answer('Do you feel weak? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def shortness_of_breath(self):
        self.declare(Symptom(shortness_of_breath=get_answer('Do you have a short breath? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def dizziness(self):
        self.declare(Symptom(dizziness=get_answer('Do you suffer from dizziness? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def lightheadedness(self):
        self.declare(Symptom(lightheadedness=get_answer('Do you suffer from lightheadedness? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def chest_pain(self):
        self.declare(Symptom(chest_pain=get_answer('Do you feel chest pain? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def cold_hands(self):
        self.declare(Symptom(cold_hands=get_answer('Do you feel cold hands? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def cold_feet(self):
        self.declare(Symptom(cold_feet=get_answer('Do you feel cold feet? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def headache(self):
        self.declare(Symptom(headache=get_answer('Do you feel headache? ')))

    @Rule(AND(Disease(ibd=yes), Fact(tested_for_anemia=no)), salience=940)
    def brittle_nails(self):
        self.declare(Symptom(brittle_nails=yes))

    @Rule(
        AND(
            Fact(tested_for_anemia=no),
            Symptom(fatigue=yes),
            Symptom(weakness=yes),
            Symptom(pale_skin=yes),
            OR(
                Symptom(tachycardia=yes),
                Symptom(chest_pain=yes),
                Symptom(shortness_of_breath=yes)
            ),
            OR(
                Symptom(dizziness=yes),
                Symptom(lightheadedness=yes),
                Symptom(headache=yes)
            ),
            Symptom(brittle_nails=yes),
            Symptom(cold_feet=yes),
            Symptom(cold_hands=yes)
        ),
        salience=1996
    )
    def anemia(self):
        # print('anemia detected')
        self.declare(Symptom(anemia=yes))

    # ******************************************************************************************************************
    # severe ulcerative colitis
    # ******************************************************************************************************************
    @Rule(Disease(ibd=yes), salience=900)
    def fever(self):
        self.declare(Symptom(fever=get_answer('Do you have fever with no evident reasons? ')))

    @Rule(Disease(ibd=yes), salience=900)
    def nausea(self):
        self.declare(Symptom(nausea=get_answer('Do you feel nauseous? ')))

    @Rule(Disease(ibd=yes), salience=900)
    def vomit(self):
        self.declare(Symptom(vomiting=get_answer('Do you vomit? ')))

    @Rule(Disease(ibd=yes), salience=900)
    def weight_loss(self):
        self.declare(Symptom(weight_loss=get_answer('Are you losing weight unexpectedly? ')))

    @Rule(Disease(ibd=yes), salience=900)
    def loss_of_appetite(self):
        self.declare(Symptom(appetite_loss=get_answer('Do you experience a loss of appetite? ')))

    @Rule(
        AND(
            Disease(uc=yes),
            NOT(Disease(mild_uc=yes)),
            Symptom(bowel_movements_per_day=bmpd_gt_5_and_lt_10),
            Symptom(blood_with_stool_frequency=bis_frequent),
            Symptom(anemia=yes),
            Symptom(weight_loss=yes),
            Symptom(appetite_loss=yes),
            OR(Symptom(fever=yes), Symptom(fever=no)),
            OR(Symptom(nausea=yes), Symptom(nausea=no)),
            OR(Symptom(vomiting=yes), Symptom(vomiting=no))
        ),
        salience=1995
    )
    def severe_ulcerative_colitis(self):
        # print('severe uc detected.')
        self.declare(Disease(severe_uc=yes))

    # ******************************************************************************************************************
    # fulminant ulcerative colitis
    # ******************************************************************************************************************

    @Rule(
        AND(
            Disease(uc=yes),
            Symptom(bowel_movements_per_day=bmpd_gt_10),
            OR(
                Symptom(blood_with_stool_frequency=bis_frequent),
                Symptom(blood_with_stool_frequency=bis_continuous)
            ),
            Symptom(anemia=yes),
            Symptom(weight_loss=yes),
            Symptom(appetite_loss=yes),
            OR(Symptom(fever=yes), Symptom(fever=no)),
            OR(Symptom(nausea=yes), Symptom(nausea=no)),
            OR(Symptom(vomiting=yes), Symptom(vomiting=no))
        ),
        salience=1994
    )
    def fulminant_ulcerative_colitis(self):
        self.declare(Disease(fulminant_uc=yes))

    # ******************************************************************************************************************
    # crohn's disease
    # ******************************************************************************************************************

    # ******************************************************************************************************************
    # mild crohn's disease
    # ******************************************************************************************************************

    @Rule(AND(NOT(Disease(uc=yes))), Disease(ibd=yes))
    def mouth_sores(self):
        self.declare(Symptom(mouth_sores=get_answer('Do you have recurrent mouth sores? ')))

    @Rule(AND(NOT(Disease(uc=yes))), Disease(ibd=yes))
    def fistula(self):
        self.declare(Symptom(fistula=get_answer('Do you have fistula? ')))

    @Rule(
        AND(
            Disease(ibd=yes),
            Symptom(tenesmus=no),
            Symptom(pus_with_stool=no),
            Symptom(mucus_with_stool=no),
            Symptom(mouth_sores=yes),
            Symptom(appetite_loss=yes),
            Symptom(weight_loss=yes),
            Symptom(fistula=yes),
            OR(
                AND(Symptom(blood_with_stool=yes),
                    # if yes, frequency depends on the location
                    OR(Symptom(blood_with_stool_frequency=L(bis_rare) | L(bis_frequent) | L(bis_continuous)))),
                Symptom(blood_with_stool=no)
            ),
            OR(Symptom(fever=yes), Symptom(fever=no))
        ),
        salience=1993
    )
    def mild_crohn_disease(self):
        # print('mild crohn symptoms detected')
        self.declare(Disease(mild_crohn=yes))

    # ******************************************************************************************************************
    # severe crohn's disease
    # ******************************************************************************************************************

    @Rule(Disease(mild_crohn=yes))
    def bumps_under_skin(self):
        self.declare(
            Symptom(red_tender_bumps_under_the_skin=get_answer('Did you notice red tender bumps under the skin? ')))

    @Rule(Disease(mild_crohn=yes))
    def eye_pain(self):
        self.declare(Symptom(eye_pain=get_answer('Do you fell eye pain? ')))

    @Rule(Disease(mild_crohn=yes))
    def eye_redness(self):
        self.declare(Symptom(eye_redness=get_answer('Do you often experience eye redness? ')))

    @Rule(Disease(mild_crohn=yes))
    def joint_pain(self):
        self.declare(Symptom(joint_pain=get_answer('Do you experience joint pain? ')))

    @Rule(Disease(mild_crohn=yes))
    def joint_soreness(self):
        self.declare(Symptom(joint_soreness=get_answer('Do you experience joint soreness? ')))

    @Rule(
        AND(
            Disease(mild_crohn=yes),
            Symptom(anemia=yes),
            Symptom(red_tender_bumps_under_the_skin=yes),
            OR(Symptom(fever=yes), Symptom(fever=no)),
            OR(Symptom(eye_pain=yes), Symptom(eye_pain=no)),
            OR(Symptom(eye_redness=yes), Symptom(eye_redness=no)),
            OR(Symptom(joint_pain=yes), Symptom(joint_pain=no)),
            OR(Symptom(joint_soreness=yes), Symptom(joint_soreness=no))
        ),
        salience=1992
    )
    def severe_crohn_disease(self):
        # print('severe crohn detected')
        self.declare(Disease(severe_crohn=yes))

    # ******************************************************************************************************************
    # conclusion
    # ******************************************************************************************************************
    @Rule(
        OR(
            AND(
                NOT(Disease(ibs=yes)),
                NOT(Disease(mild_uc=yes)),
                NOT(Disease(severe_uc=yes)),
                NOT(Disease(fulminant_uc=yes)),
                NOT(Disease(mild_crohn=yes)),
                NOT(Disease(severe_crohn=yes)),

            ),

            AND(
                NOT(Disease(ibs=yes)),
                NOT(Disease(mild_uc=yes)),
                NOT(Disease(severe_uc=yes)),
                NOT(Disease(fulminant_uc=yes)),
                NOT(Disease(mild_crohn=yes)),
                NOT(Disease(severe_crohn=yes)),
                Symptom(stool_type=None)
            ),

        )
    )
    def none_detected(self):
        self.declare(Disease(unknown=yes))
