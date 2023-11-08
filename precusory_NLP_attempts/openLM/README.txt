
####### Following commands are for attempting openLLM ##########

The following commands lead to the creation of tokenized data from the input folder, 'cliCode'
-----------------------------------------
'cliCode' gets transformed into ->
    'tokenizedFolders' ->
    'processedTokenizedData' ->
    'open_lm/datapreprocess/preproc_data'
-----------------------------------------

1. $ python tokenizeFolders.py

2. $ python open_lm/datapreprocess/process.py --output-dir processedTokenizedData

3. $ python datapreprocess/make_2048.py \
    --input-files C:/Users/at895452/Desktop/innovation/processedTokenizedData/*.jsonl
    --output-dir preproc_data
    --num-workers 32
    --num-consumers 1

4. (switching to wsl to see if works in linux env)
export CUDA_VISIBLE_DEVICES=0,1,2,3
torchrun --nproc-per-node 4 -m open_lm.main \
  --model open_lm_11m \
  --train-data /preproc_data/shard-{0000000..0000099}.tar \
  --train-num-samples 1000000000 \
  --workers 1 \
  --dataset-resampled \
  --precision amp_bfloat16 \
  --batch-size 8 \
  --grad-checkpointing \
  --log-every-n-steps 100 \
  --grad-clip-norm 1 \
  --data-key txt \
  --lr 3e-4 \
  --fsdp --fsdp-amp \
  --warmup 2000 \
  --wd 0.1 \
  --beta2 0.95 \
  --epochs 100 \
  --report-to wandb \
  --wandb-project-name open_lm_example \
  --name open_lm_ex_$RANDOM \
  --resume latest \
  --logs C:/Users/at895452/Desktop/innovation/logs



#installing CUDA toolkit... https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

