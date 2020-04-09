import pickle
with open('./config.pickle', 'rb') as f:    
	w = pickle.load(f)
	pickle.dump(w, open('./config2.pickle',"wb"), protocol=2)
