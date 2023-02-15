import random
import pandas
from utility_package.utils import *


def gen_examples(max_n: int):
    """
    Generate max_n examples for each disease and save the dataframe to a csv file.
    To simulate a real dataset the examples oc class x may include symptoms of other diseases in th scope of this
    project:
    For example if an example is classified as ibs, ibs doesn't cause anemia but with a probability of
    6% the example will include it because it may be caused by unknown factors
    :param max_n: number of examples for each disease
    """
    data = []

    print('Generating irritable bowel syndrome examples')
    for i in range(0, max_n):
        symptoms_dict_ibs0 = {
            bloating: yes,
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            abdominal_pain: yes,
            abdomen_cramps: random.choices([yes, no], weights=[6, 94])[0],
            stool_type: constipation,  # vedi
            bowel_movements_per_day: bmpd_lt_1,
            blood_with_stool_frequency: random.choices([bis_rare, bis_frequent, bis_continuous, 'None'],
                                                       weights=[10, 7, 3, 80])[0],  # vedi
            uc: no,
            ibd: no,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: ibs
        }

        symptoms_dict_ibs1 = {
            bloating: yes,
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            abdominal_pain: yes,
            abdomen_cramps: random.choices([yes, no], weights=[6, 94])[0],
            stool_type: alternate,  # vedi
            bowel_movements_per_day: bmpd_nc,
            blood_with_stool_frequency: random.choices([bis_rare, bis_frequent, bis_continuous, 'None'],
                                                       weights=[10, 7, 3, 80])[0],  # vedi
            uc: no,
            ibd: no,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: ibs
        }

        symptoms_dict_ibs2 = {
            bloating: yes,
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            abdominal_pain: yes,
            abdomen_cramps: random.choices([yes, no], weights=[6, 94])[0],
            stool_type: diarrhea,  # vedi
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices([bis_rare, 'None'],
                                                       weights=[4, 96])[0],  # vedi
            uc: no,
            ibd: no,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: ibs
        }
        dict_: dict = random.choice([symptoms_dict_ibs0, symptoms_dict_ibs1, symptoms_dict_ibs2])
        data.append(dict_)

    print('Generating mild ulcerative colitis examples')
    for i in range(0, max_n):
        symptoms_dict_mild_uc0 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: no,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices([bis_rare, 'None'],
                                                       weights=[40, 60])[0],
            uc: yes,
            ibd: yes,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: mild_uc
        }

        symptoms_dict_mild_uc1 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: no,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices([bis_rare, 'None'],
                                                       weights=[40, 60])[0],
            uc: yes,
            ibd: yes,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: mild_uc
        }

        symptoms_dict_mild_uc2 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices([bis_rare, 'None'],
                                                       weights=[40, 60])[0],
            uc: yes,
            ibd: yes,
            anemia: random.choices([yes, no], weights=[6, 94])[0],
            fever: random.choices([yes, no], weights=[6, 94])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: random.choices([yes, no], weights=[6, 94])[0],
            appetite_loss: random.choices([yes, no], weights=[6, 94])[0],
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: mild_uc
        }
        data.append(random.choice([symptoms_dict_mild_uc0, symptoms_dict_mild_uc1, symptoms_dict_mild_uc2]))

    print('Generating severe ulcerative colitis examples')
    for i in range(0, max_n):
        symptoms_dict_severe_uc0 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: no,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_5_and_lt_10,
            blood_with_stool_frequency: random.choices([bis_rare, bis_frequent, bis_continuous],
                                                       weights=[20, 70, 10])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: severe_uc
        }

        symptoms_dict_severe_uc1 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: no,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_5_and_lt_10,
            blood_with_stool_frequency: random.choices([bis_rare, bis_frequent, bis_continuous],
                                                       weights=[20, 70, 10])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: severe_uc
        }

        symptoms_dict_severe_uc2 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_5_and_lt_10,
            blood_with_stool_frequency: random.choices([bis_rare, bis_frequent, bis_continuous],
                                                       weights=[20, 70, 10])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: severe_uc
        }

        data.append(random.choice([symptoms_dict_severe_uc0, symptoms_dict_severe_uc1, symptoms_dict_severe_uc2]))

    print('Generating fulminant ulcerative colitis examples')
    for i in range(0, max_n):
        symptoms_dict_fulminant_uc0 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_10,
            blood_with_stool_frequency: random.choices([bis_frequent, bis_continuous],
                                                       weights=[20, 80])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: fulminant_uc
        }

        symptoms_dict_fulminant_uc1 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: yes,
            pus_with_stool: no,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_10,
            blood_with_stool_frequency: random.choices([bis_frequent, bis_continuous],
                                                       weights=[20, 80])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: fulminant_uc
        }

        symptoms_dict_fulminant_uc2 = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: yes,
            mucus_with_stool: no,
            pus_with_stool: yes,
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_gt_10,
            blood_with_stool_frequency: random.choices([bis_frequent, bis_continuous],
                                                       weights=[20, 80])[0],
            uc: yes,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[46, 54])[0],
            nausea: random.choices([yes, no], weights=[46, 54])[0],
            vomiting: random.choices([yes, no], weights=[46, 54])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: random.choices([yes, no], weights=[6, 94])[0],
            fistula: random.choices([yes, no], weights=[6, 94])[0],
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: fulminant_uc
        }

        data.append(
            random.choice([symptoms_dict_fulminant_uc0, symptoms_dict_fulminant_uc1, symptoms_dict_fulminant_uc2]))

    print('Generating mild crohn examples')
    for i in range(0, max_n):
        symptoms_dict_mild_crohn = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: no,
            mucus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            pus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices(['None', bis_rare, bis_frequent, bis_continuous],
                                                       weights=[25, 25, 25, 25])[0],  # depend on the location
            uc: no,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[78, 22])[0],
            nausea: random.choices([yes, no], weights=[6, 94])[0],
            vomiting: random.choices([yes, no], weights=[6, 94])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: yes,
            fistula: yes,
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[6, 94])[0],
            eye_pain: random.choices([yes, no], weights=[6, 94])[0],
            eye_redness: random.choices([yes, no], weights=[6, 94])[0],
            joint_pain: random.choices([yes, no], weights=[6, 94])[0],
            joint_soreness: random.choices([yes, no], weights=[6, 94])[0],
            diagnosis: mild_crohn
        }
        data.append(symptoms_dict_mild_crohn)

    print('Generating severe crohn examples')
    for i in range(0, max_n):
        symptoms_dict_severe_crohn = {
            bloating: random.choices([yes, no], weights=[46, 54])[0],
            tenesmus: no,
            mucus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            pus_with_stool: random.choices([yes, no], weights=[6, 94])[0],
            abdominal_pain: yes,
            abdomen_cramps: yes,
            stool_type: diarrhea,
            bowel_movements_per_day: bmpd_lt_5,
            blood_with_stool_frequency: random.choices(['None', bis_rare, bis_frequent, bis_continuous],
                                                       weights=[25, 25, 25, 25])[0],  # depend on the location
            uc: no,
            ibd: yes,
            anemia: yes,
            fever: random.choices([yes, no], weights=[78, 22])[0],
            nausea: random.choices([yes, no], weights=[46, 50])[0],
            vomiting: random.choices([yes, no], weights=[46, 50])[0],
            weight_loss: yes,
            appetite_loss: yes,
            mouth_sores: yes,
            fistula: yes,
            red_tender_bumps_under_the_skin: random.choices([yes, no], weights=[78, 22])[0],
            eye_pain: random.choices([yes, no], weights=[78, 22])[0],
            eye_redness: random.choices([yes, no], weights=[78, 22])[0],
            joint_pain: random.choices([yes, no], weights=[78, 22])[0],
            joint_soreness: random.choices([yes, no], weights=[78, 22])[0],
            diagnosis: severe_crohn
        }
        data.append(symptoms_dict_severe_crohn)

    return pandas.DataFrame.from_records(data)


if __name__ == '__main__':
    n = 10000  # examples for disease
    dataframe = gen_examples(n)
    dataframe = dataframe.sample(frac=1)
    dataframe.replace([True], 1, inplace=True)
    dataframe.replace([False], 0, inplace=True)

    dataframe.to_csv('new' + str(len(dataframe)) + '.csv', index=False)
