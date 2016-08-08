import pytest
from fakearray import calcium_imaging

def test_calcium_imaging_data():
	data, series, truth = calcium_imaging(shape=(100,300), n=5, t=50, seed=42, noise=0.5, withparams=True)
	assert data.shape[0]==50
	assert data.shape[1]==100
	assert data.shape[2]==300

def test_calcium_imaging_truth():
	data, series, truth = calcium_imaging(shape=(100,300), n=5, t=50, seed=42, noise=0.5, withparams=True)
	assert [[coord[0] in range(0,data.shape[1]) and coord[1] in range(0,data.shape[2]) for coord in neuron]for neuron in truth]