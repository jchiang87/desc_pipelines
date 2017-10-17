inst_dir=$( cd $(dirname $BASH_SOURCE); pwd -P )
echo ${inst_dir}
export PYTHONPATH=${inst_dir}/python:${PYTHONPATH}
