from scipy import stats


def score_point(score):
	user_score = score
	array = np.array([0,0,0])
	z_score = stats.zscore(array)
	#get current user pk 
	#find the current user zscore
	user_zscore=0
	user_points = 1+2*0
	return user_points