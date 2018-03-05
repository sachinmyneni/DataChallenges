df = pd.read_excel('state_M2016_df.xlsx',header=0,encoding=sys.getfilesystemencoding())
df.loc[df.OCC_CODE=='25-2022',['STATE','TOT_EMP','A_MEAN']].sort('A_MEAN').reset_index(drop=True)
df.loc[df.OCC_CODE=='25-2011',['STATE','A_MEAN','A_MEDIAN','A_PCT10','A_PCT25','A_PCT75','A_PCT90']].sort('A_MEDIAN').reset_index(drop=True).plot()
