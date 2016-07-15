import pytest
from fakearray import calcium_imaging

def test_calcium_imaging():
	data, series, truth = calcium_imaging(shape=(100,300), n=5, t=50, seed=42, noise=0.5, withparams=True)
	assert data.shape[0]==50
	assert data.shape[1]==100
	assert data.shape[2]==300