# deepscent
Deep learning for classifying the time series sensor data generated by cancer detection dogs

[![Build Status](https://travis-ci.com/Withington/deepscent.svg?branch=master)](https://travis-ci.com/Withington/deepscent)
[![Coverage Status](https://coveralls.io/repos/github/Withington/deepscent/badge.svg?branch=master)](https://coveralls.io/github/Withington/deepscent?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Withington/deepscent/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Withington/deepscent/?branch=master)

# Data
Sample data has been obtained from the [UEA & UCR Time Series 
Classification Repository](http://www.timeseriesclassification.com 
"timeseriesclassification.com").

 Anthony Bagnall, Jason Lines, Aaron Bostrom, James Large and Eamonn 
 Keogh, The Great Time Series Classification Bake Off: a Review and 
 Experimental Evaluation of Recent Algorithmic Advances, Data Mining 
 and Knowledge Discovery, 31(3), 2017". [Paper link.](https://link.springer.com/article/10.1007/s10618-016-0483-9 
 "Bagnall et al. (2017)")
 
 Dummy data is used to represent cancer detection dogs' data. It in no way reflects the true data collected.

# Prerequisites
TensorFlow - For GPU support, TensorFlow recommends using their Docker 
image to simplify installation and avoid library conflicts (Linux only).

Follow [Tensorflow's instuctions](https://www.tensorflow.org/install/gpu "TensorFlow Docker")
 to install Docker and nvidia-docker.

# Run
```
cd deepscent
```
The command below runs a Docker container with tensorflow configured to 
run on GPUs, mounts volumes and launches Jupyter Notebook.
```
docker run --runtime=nvidia -it \
--name deepscent \
-v "$(pwd)"/notebooks:/notebooks/deepscent/notebooks \
-v "$(pwd)"/data:/notebooks/deepscent/data:ro \
-v "$(pwd)"/logs:/notebooks/deepscent/logs \
-p 8888:8888 tensorflow/tensorflow:latest-gpu-py3
```
This returns a ULR where you can open the Jupyter Notebook. Navigate 
to notebooks/deepscent/notebooks and open mlp.ipynb.

## Alternative - run on CPU
Alternative docker run options -
```
docker run -it \
--name deepscent \
-v "$(pwd)"/notebooks:/notebooks/deepscent/notebooks \
-v "$(pwd)"/data:/notebooks/deepscent/data:ro \
-v "$(pwd)"/logs:/notebooks/deepscent/logs \
-p 8888:8888 tensorflow/tensorflow:latest-py3
```

