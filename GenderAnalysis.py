
import pandas
import numpy
import matplotlib 
import datetime
from YouthSmokingAnalysis2 import YouthSmokingAnalysis2
class GenderAnalysis(YouthSmokingAnalysis2):
    
    def __init__(self):
        YouthSmokingAnalysis2.__init__(self)
    def analyze(self):
        yearandGenderGroup=self.ytsDataFrame[(self.ytsDataFrame.Gender!='Overall')
                                             & (self.ytsDataFrame.TopicDesc=='Cigarette Use (Youth)' )
                                             & (self.ytsDataFrame.MeasureDesc=='Smoking Status') & (self.ytsDataFrame.Response=='Ever')]
        yearandGenderGroup["NumberOfPeople"]=(yearandGenderGroup.Data_Value*yearandGenderGroup.Sample_Size)/100
        print(yearandGenderGroup[['YEAR','Gender','Data_Value','Sample_Size','NumberOfPeople']])
        numberOfPeopleSmoking=yearandGenderGroup.groupby(['YEAR','Gender'], as_index=False)['NumberOfPeople'].sum()
        pivotTable=pandas.pivot_table(numberOfPeopleSmoking, index=['YEAR'], columns=['Gender'] , values='NumberOfPeople')


        print(numberOfPeopleSmoking)
        print(pivotTable)

a=GenderAnalysis()
a.analyze()
