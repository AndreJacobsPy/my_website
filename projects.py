import streamlit as st

def recommendation_engine() -> None:
    st.markdown(
        '''
        ### My Job Recommendation System

        #### Description:

        This was a project developed as part of my work with a startup, Snapbrillia. The intent of this project
        was to build a recommendation engine with data found online to build a proof of concept for the actual model 
        implemented within our app.

        The goal of this project was to create a system where a model could give job recommendations based on the skills
        that a candidate has. This was done by using a classifier that would predict a job title then give an ordered list 
        of top 10 jobs by cosine simularity or how similar the other jobs were to the prediction.

        GitHub link:
        https://github.com/AndreJacobsPy/DataProjects/blob/main/recommendation%20engine/main.ipynb

        Some highlights:
        '''
    )

    st.code(
        '''
        class RecommenderModel:
                
                def __init__(self, dataframe, target, prediction_string):
                    self.dataframe = dataframe
                    self.target = target
                    self.prediction_string = prediction_string

                def split(self):
                    assert self.target in self.dataframe.columns

                    X = self.dataframe.drop(self.target, axis=1)
                    y = self.dataframe[self.target]

                    return X, y

                def train(self, soup):
                    vectorizer = CountVectorizer(stop_words='english')
                    matrix = vectorizer.fit_transform(soup)
                    cos = cosine_similarity(matrix, matrix)

                    return cos

                def check_prediction(self):
                    if self.prediction_string not in self.dataframe[self.target]:
                        possible_names = [x for x in self.dataframe[self.target] if self.prediction_string in x]
                        names_length = [len(x) for x in possible_names]

                        min_value = min(names_length)

                        index = names_length.index(min_value)

                        return possible_names[index]

                    else:
                        return self.prediction_string

                    
                def predict_bounties(self, X, y, cos):
                    prediction_updated = self.check_prediction()

                    bounty_names = pd.Series(y.index, index=y)
                    title = bounty_names[prediction_updated]

                    if type(title) == pd.Series:
                        title = title[0]

                    scores = list(enumerate(cos[title]))
                    scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

                    displayed_scores = scores_sorted[0:11]
                    bounties = [i[0] for i in displayed_scores]

                    return self.dataframe[self.target].iloc[bounties]


            my_steps = [
                ('cnt_vec', CountVectorizer(stop_words='english')),
                ('naive_bayes', MultinomialNB())
            ]
            my_pipeline = Pipeline(my_steps)

            X = user_soup
            y = users['job']

            my_pipeline.fit(X, y)
            prediction = my_pipeline.predict(['python sql r'])[0]
            prediction

            recommender = RecommenderModel(df, 'title', prediction)
            X, y = recommender.split()
            cos = recommender.train(soup)
            predictions = recommender.predict_bounties(X, y, cos)
        ''', language='python'
    )

    st.markdown(
        '''
        Example output from model:

            665     Global Head of Strategy and Operations, Brand ...
            890     Global Head of Strategy and Operations, Brand ...
            1103    Manager, Online Hiring Strategy & Inbound Mark...
            670     Brand and Creative Strategist, Brand Studio (A...
            33                        Chief of Staff, Google Hardware
            874                       Chief of Staff, Google Hardware
            889     Strategy and Operations Manager, Consumer Hard...
            454     Publisher Intelligence Analyst, Online Partner...
            891        SMB Sales Manager, International, Google Cloud
            626     Associate Product Marketing Manager Program (A...
            133                      Manager, Performance Specialists
        '''
    )