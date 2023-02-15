from ExpertSystem.KB import *
from BayesNet.BNGastroenterologyDiagnosticTool import BNGastroenterologyDiagnosticTool

# watch('FACTS', 'RULES')

ibs_url = 'https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/definition-facts'
uc_url = 'https://www.niddk.nih.gov/health-information/digestive-diseases/ulcerative-colitis/definition-facts'
crohn_url = 'https://www.niddk.nih.gov/health-information/digestive-diseases/crohns-disease/definition-facts'


def print_diagnosis(class_, evidence_, probability=None):
    url = ''
    disease_str = ''
    print()
    print(evidence_)
    if class_ == ibs:
        url = ibs_url
        disease_str = 'Irritable Bowel Syndrome'
    elif class_ == mild_uc:
        url = uc_url
        disease_str = 'Mild Ulcerative Colitis'
    elif class_ == severe_uc:
        url = uc_url
        disease_str = 'Severe Ulcerative Colitis'
    elif class_ == fulminant_uc:
        url = uc_url
        disease_str = 'Fulminant Ulcerative Colitis'
    elif class_ == mild_crohn:
        url = crohn_url
        disease_str = 'Mild crohn\'s Disease'
    elif class_ == severe_crohn:
        url = crohn_url
        disease_str = 'Severe crohn\'s Disease'

    if probability is None and class_ != unknown:
        print(f'The system detected a form of {disease_str}.\n'
              f'For more information visit the following page of the U.S. institute of Diabetes and '
              f'and Kidney Disease: \n'
              f'{url}')
    elif probability is not None and probability != -1:
        print(f'The system detected a form of {disease_str} with probability {probability * 100}.\n'
              f'For more information visit the following page of the U.S. institute of Diabetes and '
              f'and Kidney Disease: \n'
              f'{url}')
    elif class_ == unknown or probability == -1:
        print(f'Based on the symptoms above the system can\'t detect a disease.\n'
              f'The patient may be healthy or affected by diseases for which the system is not trained. ')


if __name__ == '__main__':
    mode = ''

    while True:
        mode = input('Choose a way to use the system:\n'
                     '1) use KB + BBN\n'
                     '     the system use the KB, if the KB can\'t recognize the disease put declared facts as '
                     ' evidence for the BBN\n'
                     '2) use KB only\n'
                     '3) use BBN only\n')
        if mode.isnumeric():
            if int(mode) in range(1, 4):
                mode = int(mode)
                break

    if mode == 1:
        engine = ES()
        engine.reset()
        engine.run()

        disease = None
        prob = None

        print('\n\n\n\n\n\n\n\n\n\n')
        print(engine.facts)
        print('\n\n\n\n\n\n\n\n\n\n')
        evidence = {}
        disease_list = [ibs, mild_uc, severe_uc, fulminant_uc, mild_crohn, severe_crohn]
        symptoms_list = [
            bloating, tenesmus, mucus_with_stool, pus_with_stool, abdominal_pain, abdomen_cramps, stool_type,
            bowel_movements_per_day, blood_with_stool_frequency, anemia, fever, nausea, vomiting,
            weight_loss, appetite_loss, mouth_sores, fistula, red_tender_bumps_under_the_skin, eye_pain,
            eye_redness, joint_pain, joint_soreness, uc, ibd,
        ]
        for index in range(len(engine.facts)):
            for key in engine.facts[index]:
                if key in disease_list:
                    # evidence[key] = engine.facts[index][key]
                    disease = key
                    break
                elif key == stool_type and engine.facts[index][key] is None:
                    disease = unknown
                    break
                elif key in symptoms_list:
                    evidence[key] = engine.facts[index][key]
                elif key == blood_with_stool and engine.facts[index][key] == no:
                    evidence[blood_with_stool_frequency] = 'None'

        if disease is None:
            if (stool_type, alternate) in evidence:
                evidence[bowel_movements_per_day] = bmpd_nc
            if (stool_type, constipation) in evidence:
                evidence[bowel_movements_per_day] = bmpd_lt_1
            if bowel_movements_per_day not in evidence:
                evidence[bowel_movements_per_day] = bmpd_lt_5

            for key, value in evidence.items():
                if value is True:
                    evidence[key] = 1
                elif value is False:
                    evidence[key] = 0

            try:
                model = BNGastroenterologyDiagnosticTool()
                model.plot_dag()
                model.load_data()
                model.create_model()
                disease, prob = model.make_inference(evidence)
            except:
                disease = unknown

        print_diagnosis(disease, evidence, prob)
    elif mode == 2:
        engine = ES()
        engine.reset()
        engine.run()

        disease = None

        print('\n\n\n\n\n\n\n\n\n\n')
        print(engine.facts)
        print('\n\n\n\n\n\n\n\n\n\n')
        disease_list = [ibs, mild_uc, severe_uc, fulminant_uc, mild_crohn, severe_crohn, unknown]
        for index in range(len(engine.facts)):
            for key in engine.facts[index]:
                if key in disease_list:
                    # evidence[key] = engine.facts[index][key]
                    disease = key
                    break

        print_diagnosis(disease, engine.facts)


    elif mode == 3:
        disease = None
        prob = None
        evidence = {
            bloating: get_answer('Are you feeling bloated? '),
            tenesmus: get_answer('Do you suffer from tenesmus? '),
            mucus_with_stool: get_answer('Do you observe mucus with your stool? '),
            pus_with_stool: get_answer('Do you observe pus in your stool? '),
            abdominal_pain: get_answer('Do you experience abdominal pain? '),
            abdomen_cramps: get_answer('Do you experience abdominal cramps? '),
            stool_type: get_answer('Do you suffer from\n'
                                   '1)diarrhea,\n'
                                   '2)constipation,\n'
                                   '3)both alternate,\n',
                                   stool_dict),
            # bowel_movements_per_day: bmpd_lt_1,
            blood_with_stool_frequency: get_answer('\nHow often do you observe blood with stool?\n'
                                                   '1) Continuously,\n'
                                                   '2) Most of the time,\n'
                                                   '3) Rarely\n'
                                                   '4) Never\n'
                                                   , bis_dict1),

            anemia: get_answer('Do you suffer from anemia? '),
            fever: get_answer('Do you have fever with no evident reasons? '),
            nausea: get_answer('Do you feel nauseous? '),
            vomiting: get_answer('Do you vomit? '),
            weight_loss: get_answer('Are you losing weight unexpectedly? '),
            appetite_loss: get_answer('Do you experience a loss of appetite? '),
            mouth_sores: get_answer('Do you have recurrent mouth sores? '),
            fistula: get_answer('Do you have fistula? '),
            red_tender_bumps_under_the_skin: get_answer('Did you notice red tender bumps under the skin? '),
            eye_pain: get_answer('Do you fell eye pain? '),
            eye_redness: get_answer('Do you often experience eye redness? '),
            joint_pain: get_answer('Do you experience joint pain? '),
            joint_soreness: get_answer('Do you experience joint soreness? '),
        }

        if evidence[stool_type] == constipation:
            evidence[bowel_movements_per_day] = bmpd_lt_1
        elif evidence[stool_type] == alternate:
            evidence[bowel_movements_per_day] = bmpd_nc
        else:
            evidence[bowel_movements_per_day] = get_answer('How often do you need to have a bowel movement?\n'
                                                           '1) > 2 and <= 5 per day,\n'
                                                           '2) > 5 and < 10 per day,\n'
                                                           '3) >= 10 per day\n', bmpd_dict)

        for key, value in evidence.items():
            if value is True:
                evidence[key] = 1
            elif value is False:
                evidence[key] = 0
        try:
            model = BNGastroenterologyDiagnosticTool()
            model.plot_dag()
            model.load_data()
            model.create_model()
            disease, prob = model.make_inference(evidence)
        except:
            disease = unknown

        print_diagnosis(disease, evidence, prob)
