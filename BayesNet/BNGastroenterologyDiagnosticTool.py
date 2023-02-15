import pandas
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold

from utility_package.utils import *
import bnlearn


class BNGastroenterologyDiagnosticTool:
    """
    A diagnostic tool to identify gastroenterological disease given the symptoms
    """

    def __init__(self):
        self.model = None
        self.df = None
        self.path_to_data = 'BayesNet/Dataset/GastroenterologyDisease60k.csv'
        self.model_name = 'model'
        self.path_to_model = 'BayesNet/Model/'

        self.edges = [
            # irritable bowel disease
            (bloating, ibs),
            (tenesmus, ibs),
            (mucus_with_stool, ibs),
            (abdominal_pain, ibs),
            (stool_type, ibs),
            (blood_with_stool_frequency, ibs),
            # dependency between the bleeding given the stool type
            (stool_type, blood_with_stool_frequency),
            # inflammable bowel disease
            (bloating, ibd),
            (stool_type, ibd),
            (abdominal_pain, ibd),
            (abdomen_cramps, ibd),
            # ulcerative colitis
            (ibd, uc),
            (mucus_with_stool, uc),
            (pus_with_stool, uc),
            (tenesmus, uc),
            # mild ulcerative colitis
            (uc, mild_uc),
            (bowel_movements_per_day, mild_uc),
            (blood_with_stool_frequency, mild_uc),
            # dependency of the weight loss given the appetite loss
            (appetite_loss, weight_loss),
            # severe ulcerative colitis
            (uc, severe_uc),
            (bowel_movements_per_day, severe_uc),
            (blood_with_stool_frequency, severe_uc),
            (anemia, severe_uc),
            (weight_loss, severe_uc),
            (fever, severe_uc),
            (vomiting, severe_uc),
            (nausea, severe_uc),
            # fulminant ulcerative colitis
            (uc, fulminant_uc),
            (bowel_movements_per_day, fulminant_uc),
            (blood_with_stool_frequency, fulminant_uc),
            (anemia, fulminant_uc),
            (weight_loss, fulminant_uc),
            (appetite_loss, fulminant_uc),
            (fever, fulminant_uc),
            (vomiting, fulminant_uc),
            (nausea, fulminant_uc),
            # mild crohn
            (ibd, mild_crohn),
            (mouth_sores, mild_crohn),
            (weight_loss, mild_crohn),
            (fistula, mild_crohn),
            (blood_with_stool_frequency, mild_crohn),
            (fever, mild_crohn),
            # severe crohn
            (ibd, severe_crohn),
            (mouth_sores, severe_crohn),
            (weight_loss, severe_crohn),
            (fistula, severe_crohn),
            (blood_with_stool_frequency, severe_crohn),
            (fever, severe_crohn),
            (anemia, severe_crohn),
            (red_tender_bumps_under_the_skin, severe_crohn),
            (eye_pain, severe_crohn),
            (eye_redness, severe_crohn),
            (joint_pain, severe_crohn),
            (joint_soreness, severe_crohn)
        ]
        self.dag = bnlearn.make_DAG(self.edges)

    def plot_dag(self):
        bnlearn.plot(self.dag, interactive=True)

    def load_data(self, path_to_data=None):
        """
        Load the dataset and prepare it for the bayesian network adding a column (1, 0) for each disease
        :param path_to_data: path where the dataset is stored
        """
        # loading data
        if path_to_data is not None:
            self.df = pandas.read_csv(path_to_data)
        else:
            self.df = pandas.read_csv(self.path_to_data)

        # adding the column representing each disease
        ibs_l = []
        mild_uc_l = []
        severe_uc_l = []
        fulminant_uc_l = []
        mild_crohn_l = []
        severe_crohn_l = []
        for i in range(0, len(self.df)):
            example = self.df.iloc[i]
            if example[diagnosis] == ibs:
                ibs_l.append(1)
                mild_uc_l.append(0)
                severe_uc_l.append(0)
                fulminant_uc_l.append(0)
                mild_crohn_l.append(0)
                severe_crohn_l.append(0)
            elif example[diagnosis] == mild_uc:
                ibs_l.append(0)
                mild_uc_l.append(1)
                severe_uc_l.append(0)
                fulminant_uc_l.append(0)
                mild_crohn_l.append(0)
                severe_crohn_l.append(0)
            elif example[diagnosis] == severe_uc:
                ibs_l.append(0)
                mild_uc_l.append(0)
                severe_uc_l.append(1)
                fulminant_uc_l.append(0)
                mild_crohn_l.append(0)
                severe_crohn_l.append(0)
            elif example[diagnosis] == fulminant_uc:
                ibs_l.append(0)
                mild_uc_l.append(0)
                severe_uc_l.append(0)
                fulminant_uc_l.append(1)
                mild_crohn_l.append(0)
                severe_crohn_l.append(0)
            elif example[diagnosis] == mild_crohn:
                ibs_l.append(0)
                mild_uc_l.append(0)
                severe_uc_l.append(0)
                fulminant_uc_l.append(0)
                mild_crohn_l.append(1)
                severe_crohn_l.append(0)
            elif example[diagnosis] == severe_crohn:
                ibs_l.append(0)
                mild_uc_l.append(0)
                severe_uc_l.append(0)
                fulminant_uc_l.append(0)
                mild_crohn_l.append(0)
                severe_crohn_l.append(1)
        self.df[ibs] = ibs_l
        self.df[mild_uc] = mild_uc_l
        self.df[severe_uc] = severe_uc_l
        self.df[fulminant_uc] = fulminant_uc_l
        self.df[mild_crohn] = mild_crohn_l
        self.df[severe_crohn] = severe_crohn_l
        return self.df

    def create_model(self, custom_data=None):
        """
        Given the directed acyclic graph and the dataset, calculates the Conditional probability distribution using
        the bayesian estimator:
            The bayesian estimator starts with already existing prior CPDs, those prior will be updated using state
            counts from the observed data.
            It starts with already existing prior CPDs, that express beliefs about the variables before observing data.
            Those "priors" are then updated, using the state counts from the observed data.
                Priors of conditional probability tables are calculated using BDeu (Bayesian Dirichlet equivalent
                uniform), for each node in the network.
                To calculate the BDeu prior for a CPT the equivalent sample size (ESS) must be set, in bnlearn is 1000,
                the ESS is the number of pseudo counts that are added to the observed counts in the data.

                For each possible combination of values of the node's parents the BDeu score is calculated and then the
                prior probabilities of the CPT.
                These prior probabilities are combined with the observed data to compute the posterior probabilities
                using Bayes' rule.

                Using this method with a high ESS prevent overfitting.
        """
        if self.model is not None:
            self.model = None
        if custom_data is not None:
            self.model = bnlearn.parameter_learning.fit(self.dag, custom_data, methodtype='bayes', scoretype='bdeu',
                                                        verbose=0)
        else:
            self.model = bnlearn.parameter_learning.fit(self.dag, self.df, methodtype='bayes', scoretype='bdeu',
                                                        verbose=0)

    def load_model(self, model_name):
        """Load an existing model"""
        self.model = bnlearn.load(self.path_to_model + model_name + '.pkl')
        return self.model

    def save_model(self, model_name):
        """Save the model to a .pkl file in the folder Model."""
        bnlearn.save(self.model, self.path_to_model + model_name, overwrite=True)

    def make_inference(self, evidence):
        """
        Makes a prediction for each disease given the evidences.
        :param evidence: a dict containing all the positive evidence
        for example
                '{tenesmus': 1,
                'pus_with_stool': 1,
                'abdomen_cramps': 1,
                'stool_type': 'diarrhea',
                'bowel_movements_per_day': '>= 10 per day',
                'blood_with_stool_frequency': 'Continuous',
                'uc': 1,
                'ibd': 1,
                'anemia': 1,
                'fever': 1,
                'nausea': 1,
                'vomiting': 1,
                'weight_loss': 1,
                'appetite_loss': 1,}
        :return: (not classified, -1) if the example could not be classified, (disease, probability) else
        """
        query_ibs = bnlearn.inference.fit(self.model, variables=[ibs], evidence=evidence, verbose=0)
        query_muc = bnlearn.inference.fit(self.model, variables=[mild_uc], evidence=evidence, verbose=0)
        query_suc = bnlearn.inference.fit(self.model, variables=[severe_uc], evidence=evidence, verbose=0)
        query_fuc = bnlearn.inference.fit(self.model, variables=[fulminant_uc], evidence=evidence, verbose=0)
        query_mcrohn = bnlearn.inference.fit(self.model, variables=[mild_crohn], evidence=evidence, verbose=0)
        query_scrohn = bnlearn.inference.fit(self.model, variables=[severe_crohn], evidence=evidence, verbose=0)

        positive_ibs = query_ibs.df['p'][1]
        positive_muc = query_muc.df['p'][1]
        positive_suc = query_suc.df['p'][1]
        positive_fuc = query_fuc.df['p'][1]
        positive_mcrohn = query_mcrohn.df['p'][1]
        positive_scrohn = query_scrohn.df['p'][1]

        max_ = max(positive_ibs, positive_muc, positive_suc, positive_fuc, positive_mcrohn, positive_scrohn)

        if positive_ibs == positive_muc == positive_suc == positive_fuc == positive_mcrohn == positive_scrohn:
            # if no prediction has been made
            print(evidence)
            print(query_ibs)
            print(query_muc)
            print(query_suc)
            print(query_fuc)
            print(query_mcrohn)
            print(query_scrohn)
            print('The system can\'t evaluate this evidence')
            return 'not classified', -1
        else:
            if max_ == positive_ibs:
                return ibs, max_
            elif max_ == positive_muc:
                return mild_uc, max_
            elif max_ == positive_suc:
                return severe_uc, max_
            elif max_ == positive_fuc:
                return fulminant_uc, max_
            elif max_ == positive_mcrohn:
                return mild_crohn, max_
            elif max_ == positive_scrohn:
                return severe_crohn, max_


def k_fold_validation(k: int):
    k_fold = KFold(n_splits=k, shuffle=False, random_state=None)
    target_names = [ibs, mild_uc, severe_uc, fulminant_uc, mild_crohn, severe_crohn]
    model = BNGastroenterologyDiagnosticTool()
    df = model.load_data()
    iterator = k_fold.split(model.df)
    y_true = []
    y_pred = []
    for i in range(0, k):
        print(f'Fold {i}')
        result = next(iterator)
        train = df.iloc[result[0]]
        test = df.iloc[result[1]]
        print(f'test set len:_______{len(test)}')
        model.create_model(train)
        test = test.T
        for j in test:
            example = test.pop(j)
            target = example[diagnosis]
            example.drop(labels=[ibs, mild_crohn, severe_crohn, fulminant_uc, mild_uc, severe_uc, diagnosis],
                         inplace=True)
            # example = example[~(example == 0)]
            print(example.to_dict())
            class_, probability = model.make_inference(evidence=example)
            if probability == -1:
                print(f'This evidence must be classified as {target}')
                for c in target_names:
                    if target != c:
                        y_true.append(target)
                        y_pred.append(c)
            else:
                y_true.append(target)
                y_pred.append(class_)
    report = classification_report(y_true, y_pred, target_names=target_names)
    print(f'\n\n{report}')


# k_fold_validation(10)
