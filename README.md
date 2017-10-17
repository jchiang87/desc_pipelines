# desc_pipelines

This package contains some tools to help design and implement DESC
Science Pipelines.

## Installation
From the top-level directory, in your bash shell, do
```
$ source ./setup.sh
```
This will modify your PYTHONPATH.

## Pipeline DAG example
The Strong Lensing pipeline diagram shown at the
2017 Stony Brook DESC meeting [Pipeline design session](https://confluence.slac.stanford.edu/display/LSSTDESC/Pipeline+design+session) was implemented in
[examples/sl_pipeline.py](/examples/sl_pipeline.py).   The resulting DAG was via
```
$ python sl_pipeline.py
```

![SLPipeline DAG][/examples/SLPipeline.png]
