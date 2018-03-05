df = pd.read_excel('state_M2016_df.xlsx',header=0,encoding=sys.getfilesystemencoding())
df.loc[df.OCC_CODE=='25-2022',['STATE','TOT_EMP','A_MEAN']].sort('A_MEAN').reset_index(drop=True)
